# Firstep Compatibility Chatbot Demo

A sophisticated Dialogflow-powered chatbot demonstrating explainable AI for family planning compatibility matching. This project showcases rule-based recommendation systems, natural language processing, and transparent algorithmic decision-making.

## Project Overview

This demo addresses the job requirements for the AI Engineer Intern position at Firstep, demonstrating:

- **Dialogflow Integration**: Conversational AI with intent recognition and entity extraction
- **Rule-Based Matching**: Sophisticated compatibility scoring algorithms
- **Explainable AI**: Transparent reasoning for all recommendations
- **Real-Time Processing**: Dynamic user profiling and matching
- **Family Planning Focus**: Values-based compatibility for intentional family formation

## Quick Start

### Prerequisites
- Python 3.8+
- Git
- Web browser

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Dialogflow-Chatbot-Demo
   ```

2. **Set up Python environment:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the backend server:**
   ```bash
   python app.py
   ```

4. **Open the demo:**
   - Navigate to `http://localhost:5000` in your browser
   - Click "Start Onboarding Demo" to begin
   - Or click "Skip to Matching Demo" to see results

## Key Features

### 1. Conversational Onboarding
- Natural language collection of user preferences
- Progressive profiling through dialogue
- Entity extraction for structured data

### 2. Multi-Dimensional Compatibility Scoring
- **Values Alignment** (35% weight): Core life priorities
- **Family Goals** (30% weight): Shared vision for family structure
- **Communication Style** (20% weight): Interaction preferences
- **Timeline Compatibility** (15% weight): Family planning timing

### 3. Explainable Recommendations
- Detailed breakdowns of compatibility scores
- Human-readable explanations for each match
- Transparent algorithmic reasoning
- Actionable next steps

### 4. Advanced Message Formatting
- **Line Break Support**: Converts `\n` to HTML `<br>` tags for proper display
- **Markdown Rendering**: Converts `**bold**` text to HTML `<strong>` elements
- **Rich Text Display**: Supports formatted compatibility results and explanations

### 5. Rule-Based Logic
```python
# Example compatibility calculation
def calculate_compatibility(user1, user2):
    values_score = calculate_values_alignment(user1.values, user2.values)
    goals_score = calculate_goals_overlap(user1.goals, user2.goals)
    comm_score = calculate_communication_compatibility(user1.style, user2.style)
    timeline_score = calculate_timeline_alignment(user1.timeline, user2.timeline)
    
    overall = (values_score * 0.35 + goals_score * 0.30 + 
               comm_score * 0.20 + timeline_score * 0.15)
    
    return CompatibilityScore(overall, explanation)
```

## Demo Flow

### Phase 1: User Onboarding
1. **Basic Information**: Name, age, location
2. **Values Assessment**: 8 core values rated 1-5
3. **Family Goals**: Multiple selection from predefined options
4. **Communication Style**: Single selection from 5 styles
5. **Timeline Preference**: Family planning timeline

### Phase 2: Matching & Explanation
1. **Match Generation**: Top 3 compatible profiles
2. **Score Presentation**: Percentage compatibility with reasoning
3. **Detailed Explanation**: Breakdown by dimension
4. **Next Steps**: Actionable recommendations

## Technical Implementation

### Backend Components

**`models.py`**: Data structures for users and compatibility scores
```python
@dataclass
class UserProfile:
    user_id: str
    values: Dict[str, int]  # 1-5 importance scores
    family_goals: List[str]
    communication_style: str
    timeline: str
```

**`matching.py`**: Core compatibility algorithms
- Weighted scoring system
- Rule-based compatibility logic
- Explainable result generation

**`explain.py`**: Explanation generation engine
- Human-readable interpretations
- Strength/weakness identification
- Next step recommendations

**`app.py`**: Flask server with Dialogflow webhook
- Intent routing and processing
- Session management
- Response formatting

### Dialogflow Configuration

**Intents:**
- `welcome`: Initial greeting and onboarding start
- `collect.basic.info`: Name, age, location capture
- `collect.values`: Values importance scoring
- `collect.family.goals`: Family planning goals
- `collect.communication.style`: Communication preferences
- `collect.timeline`: Family planning timeline
- `find.matches`: Match generation trigger
- `explain.match`: Detailed explanations

**Entities:**
- `@family_goals`: Structured family planning options
- `@communication_style`: Communication preference types
- `@timeline`: Timeline preference categories

## Compatibility Algorithm

### Scoring Methodology

1. **Values Compatibility**:
   - Calculates alignment on shared values
   - Considers importance ratings (1-5 scale)
   - Normalizes differences to 0-1 score

2. **Goals Compatibility**:
   - Measures overlap in family planning goals
   - Uses Jaccard similarity for set comparison
   - Accounts for goal priority weighting

3. **Communication Compatibility**:
   - Predefined compatibility matrix
   - Complementary styles score higher
   - Conflicting styles identified

4. **Timeline Compatibility**:
   - Proximity-based scoring
   - Flexible timing bonus
   - Significant gaps penalized

### Explainability Features

- **Transparent Scoring**: All calculations are visible
- **Plain Language**: No technical jargon in explanations
- **Actionable Insights**: Specific next steps provided
- **Comparative Analysis**: Strengths vs. considerations
- **Trust Building**: Clear reasoning for recommendations

## Frontend Experience

### Modern UI Design
- **Tailwind CSS**: Utility-first CSS framework for rapid development
- **Glass Morphism**: Modern translucent card design with backdrop blur
- **Gradient Backgrounds**: Dynamic color gradients for visual appeal
- **Responsive Design**: Mobile-first approach with responsive breakpoints
- **Smooth Animations**: Bounce effects, hover transitions, and loading states

### Interactive Demo
- **Progressive Disclosure**: Information collected step-by-step
- **Real-Time Feedback**: Immediate responses to inputs with typing indicators
- **Formatted Messages**: Proper line breaks and bold text rendering
- **Visual Status Tracking**: Progress indicators and status updates
- **Accessible Interface**: Clean, professional design optimized for usability

### Demo Controls
- **Start Onboarding**: Full experience walkthrough
- **Skip to Matching**: See results immediately
- **Reset Chat**: Start over with new session

### Technical Skills Demonstrated
- **Dialogflow Expertise**: Intent design, entity extraction, webhook integration
- **Python Development**: Flask, data processing, algorithm implementation
- **Rule-Based Systems**: Weighted scoring, conditional logic, hybrid approaches
- **API Design**: RESTful endpoints, JSON processing, error handling
- **Modern Frontend**: Tailwind CSS, responsive design, interactive JavaScript
- **Message Formatting**: HTML/Markdown conversion, text processing, rich content display
