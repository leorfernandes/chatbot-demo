# Flask web application for compatibility chatbot demo
# Handles Dialogflow webhook integration and matching logic

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import os
from models import UserProfile, SurveyData
from matching import CompatibilityEngine
from explain import ExplainabilityEngine

# Initialize Flask app with template folder pointing to frontend
app = Flask(__name__, template_folder='../frontend')
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend

# Initialize matching and explanation engines
compatibility_engine = CompatibilityEngine()
explainability_engine = ExplainabilityEngine()

# In-memory storage for demo purposes (would use database in production)
users_db = {}          # Stores user profiles by ID
current_session = {}   # Tracks current conversation sessions

@app.route('/')
def index():
    """Serve the main chat interface HTML page"""
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def dialogflow_webhook():
    """
    Handle incoming webhook requests from Dialogflow
    
    Processes user intents and returns appropriate responses
    based on the conversation flow and user data collection
    """
    req = request.get_json()
    
    # Extract intent and parameters from Dialogflow request
    intent_name = req.get('queryResult', {}).get('intent', {}).get('displayName', '')
    parameters = req.get('queryResult', {}).get('parameters', {})
    session_id = req.get('session', '').split('/')[-1]  # Get unique session identifier
    
    # Process the intent and generate response
    response_text = handle_intent(intent_name, parameters, session_id)
    
    # Return response in Dialogflow webhook format
    return jsonify({
        'fulfillmentText': response_text
    })

def handle_intent(intent_name, parameters, session_id):
    """
    Route different intents to their appropriate handler functions
    
    Args:
        intent_name: The name of the detected Dialogflow intent
        parameters: Extracted entities/parameters from user input
        session_id: Unique identifier for this conversation session
    
    Returns:
        String response to send back to user
    """
    
    # Route to specific intent handlers
    if intent_name == 'welcome':
        return handle_welcome(session_id)
    elif intent_name == 'collect.basic.info':
        return handle_basic_info(parameters, session_id)
    elif intent_name == 'collect.values':
        return handle_values(parameters, session_id)
    elif intent_name == 'collect.family.goals':
        return handle_family_goals(parameters, session_id)
    elif intent_name == 'collect.communication.style':
        return handle_communication_style(parameters, session_id)
    elif intent_name == 'collect.timeline':
        return handle_timeline(parameters, session_id)
    elif intent_name == 'find.matches':
        return handle_find_matches(session_id)
    elif intent_name == 'explain.match':
        return handle_explain_match(parameters, session_id)
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

def handle_welcome(session_id):
    """
    Initialize a new conversation session and welcome the user
    
    Sets up session tracking and provides initial instructions
    """
    current_session[session_id] = {'step': 'welcome'}
    
    return ("Hi! I'm here to help you find meaningful family planning connections. "
            "I'll ask you some questions about your values, goals, and preferences "
            "to find compatible matches. Let's start with some basic information. "
            "What's your name?")

def handle_basic_info(parameters, session_id):
    """
    Collect and store basic user information (name, age, location)
    
    Args:
        parameters: Dict containing extracted user info from Dialogflow
        session_id: Current conversation session identifier
    
    Returns:
        Response prompting for next piece of information
    """
    if session_id not in current_session:
        current_session[session_id] = {}
    
    session_data = current_session[session_id]
    
    if 'person' in parameters and parameters['person']:
        session_data['name'] = parameters['person']['name']
        return ("Nice to meet you, {}! Now, what's your age?".format(session_data['name']))
    
    if 'age' in parameters and parameters['age']:
        session_data['age'] = int(parameters['age'])
        return ("Thanks! And what city are you located in?")
    
    if 'location' in parameters and parameters['location']:
        session_data['location'] = parameters['location']
        return ("Great! Now let's talk about your values. I'll ask about different life priorities. "
                "For each one, tell me how important it is to you on a scale of 1-5, where 5 is extremely important. "
                "How important is putting family first in your life decisions?")
    
    return "Could you please provide that information so we can continue?"

def handle_values(parameters, session_id):
    """Collect user values and priorities"""
    if session_id not in current_session:
        return "Let's start over. What's your name?"
    
    session_data = current_session[session_id]
    if 'values' not in session_data:
        session_data['values'] = {}
    
    # Map of value questions to database keys
    value_mapping = {
        'family_first': 'How important is work-life balance and career flexibility?',
        'career_balance': 'How important is financial security and stability?',
        'financial_security': 'How important is emotional intimacy and deep connection?',
        'emotional_intimacy': 'How important is shared parenting responsibilities?',
        'shared_parenting': 'How important is personal growth and self-development?',
        'personal_growth': 'How important is community involvement and social connection?',
        'community_involvement': 'How important is spiritual or philosophical alignment?'
    }
    
    if 'number' in parameters and parameters['number']:
        score = int(parameters['number'])
        values_collected = len(session_data['values'])
        value_keys = list(SurveyData.CORE_VALUES)
        
        if values_collected < len(value_keys):
            current_value = value_keys[values_collected]
            session_data['values'][current_value] = score
            
            if values_collected + 1 < len(value_keys):
                next_value = value_keys[values_collected + 1]
                return value_mapping.get(next_value, "Next value question...")
            else:
                return ("Thanks for sharing your values! Now, what are your main family planning goals? "
                        "You can mention things like biological children, adoption, co-parenting, etc.")
    
    return "Please provide a number from 1 to 5 for how important this is to you."

def handle_family_goals(parameters, session_id):
    """Collect family planning goals"""
    if session_id not in current_session:
        return "Let's start over. What's your name?"
    
    session_data = current_session[session_id]
    
    # Extract family goals from parameters (this could be more advanced with proper entity extraction)
    goals = []
    if 'family-goals' in parameters:
        goals = parameters['family-goals']
    
    session_data['family_goals'] = goals if goals else ['biological_children']  # Default
    
    return ("Got it! Now, how would you describe your communication style? "
            "Are you more direct and honest, gentle and supportive, analytical and logical, "
            "emotional and expressive, or collaborative and consensus-building?")

def handle_communication_style(parameters, session_id):
    """Collect communication style preference"""
    if session_id not in current_session:
        return "Let's start over. What's your name?"
    
    session_data = current_session[session_id]
    
    # Map communication style (would use proper entity recognition in production)
    style_mapping = {
        'direct': 'direct_honest',
        'gentle': 'gentle_supportive',
        'analytical': 'analytical_logical',
        'emotional': 'emotional_expressive',
        'collaborative': 'collaborative_consensus'
    }
    
    style = 'direct_honest'  # Default
    for key, value in style_mapping.items():
        if key in str(parameters).lower():
            style = value
            break
    
    session_data['communication_style'] = style
    
    return ("Perfect! Finally, what's your preferred timeline for starting a family? "
            "Within 1 year, 1-3 years, 3-5 years, 5+ years, or are you flexible?")

def handle_timeline(parameters, session_id):
    """Collect timeline preference and create user profile"""
    if session_id not in current_session:
        return "Let's start over. What's your name?"
    
    session_data = current_session[session_id]
    
    # Map timeline (simplified for demo)
    timeline_mapping = {
        '1 year': 'within_1_year',
        '1-3': '1_to_3_years',
        '3-5': '3_to_5_years',
        '5+': '5_plus_years',
        'flexible': 'flexible_timing'
    }
    
    timeline = 'flexible_timing'  # Default
    timeline_text = str(parameters).lower()
    for key, value in timeline_mapping.items():
        if key in timeline_text:
            timeline = value
            break
    
    session_data['timeline'] = timeline
    
    # Create user profile
    user_profile = UserProfile(
        user_id=session_id,
        name=session_data.get('name', 'Anonymous'),
        age=session_data.get('age', 30),
        location=session_data.get('location', 'Unknown'),
        values=session_data.get('values', {}),
        preferences={},
        communication_style=session_data.get('communication_style', 'direct_honest'),
        family_goals=session_data.get('family_goals', []),
        timeline=timeline
    )
    
    # Store user profile
    users_db[session_id] = user_profile
    
    return ("Perfect! I've collected all your information. Your profile is now complete. "
            "Would you like me to find some compatible matches for you?")

def handle_find_matches(session_id):
    """Find and return compatible matches"""
    if session_id not in users_db:
        return "I need to collect your information first. Let's start with your name."
    
    user = users_db[session_id]
    
    # Create sample candidates for demo
    candidates = create_sample_candidates()
    
    # Find top matches
    matches = compatibility_engine.find_top_matches(user, candidates, top_n=3)
    
    if not matches:
        return "I couldn't find any matches right now. Try expanding your criteria or check back later!"
    
    # Format response
    response = "Great! I found some compatible matches for you:\n\n"
    
    for i, match in enumerate(matches, 1):
        candidate = next(c for c in candidates if c.user_id == match.user2_id)
        response += f"{i}. {candidate.name} (Age {candidate.age}) - {int(match.overall_score * 100)}% compatibility\n"
        response += f"   Location: {candidate.location}\n"
        response += f"   Why it's a good match: {match.explanation}\n\n"
    
    response += "Would you like me to explain any of these matches in more detail?"
    
    return response

def handle_explain_match(parameters, session_id):
    """Provide detailed explanation for a specific match"""
    if session_id not in users_db:
        return "Let me collect your information first."
    
    # For demo, explain the first match
    user = users_db[session_id]
    candidates = create_sample_candidates()
    matches = compatibility_engine.find_top_matches(user, candidates, top_n=1)
    
    if not matches:
        return "No matches to explain."
    
    match = matches[0]
    explanation = explainability_engine.explain_match(match)
    
    response = f"Here's a detailed explanation of your match:\n\n"
    response += f"Overall Assessment: {explanation['overall_assessment']}\n\n"
    
    if explanation['strengths']:
        response += "Strengths:\n"
        for strength in explanation['strengths']:
            response += f"• {strength}\n"
        response += "\n"
    
    if explanation['considerations']:
        response += "Things to Consider:\n"
        for consideration in explanation['considerations']:
            response += f"• {consideration}\n"
        response += "\n"
    
    response += "This analysis helps you understand the foundation for a potential partnership. "
    response += "Would you like to see more matches or get specific advice for next steps?"
    
    return response

def create_sample_candidates():
    """Create sample candidate profiles for demo"""
    candidates = [
        UserProfile(
            user_id="candidate_1",
            name="Sarah",
            age=32,
            location="Seattle, WA",
            values={
                'family_first': 5,
                'career_balance': 4,
                'financial_security': 4,
                'emotional_intimacy': 5,
                'shared_parenting': 5,
                'personal_growth': 3,
                'community_involvement': 4,
                'spiritual_connection': 2
            },
            preferences={},
            communication_style="gentle_supportive",
            family_goals=["biological_children", "shared_parenting"],
            timeline="1_to_3_years"
        ),
        UserProfile(
            user_id="candidate_2", 
            name="Michael",
            age=29,
            location="Portland, OR",
            values={
                'family_first': 4,
                'career_balance': 5,
                'financial_security': 3,
                'emotional_intimacy': 4,
                'shared_parenting': 5,
                'personal_growth': 5,
                'community_involvement': 3,
                'spiritual_connection': 1
            },
            preferences={},
            communication_style="collaborative_consensus",
            family_goals=["biological_children", "adoption"],
            timeline="3_to_5_years"
        ),
        UserProfile(
            user_id="candidate_3",
            name="Jessica",
            age=35,
            location="San Francisco, CA", 
            values={
                'family_first': 3,
                'career_balance': 3,
                'financial_security': 5,
                'emotional_intimacy': 4,
                'shared_parenting': 4,
                'personal_growth': 4,
                'community_involvement': 5,
                'spiritual_connection': 4
            },
            preferences={},
            communication_style="analytical_logical",
            family_goals=["adoption", "blended_family"],
            timeline="within_1_year"
        )
    ]
    return candidates

@app.route('/api/test', methods=['GET'])
def test_api():
    """Test endpoint to verify API is working"""
    return jsonify({'status': 'API is working', 'message': 'Dialogflow Chatbot Demo Backend'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
