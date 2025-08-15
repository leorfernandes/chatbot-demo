# Data Files Documentation

This directory contains data files used by the compatibility chatbot for survey structure and sample data.

## Files Overview

### `sample_survey.json`
Contains the complete survey structure and sample user responses for testing.

**Structure:**
- **`survey_questions`**: Defines all survey sections and their questions
- **`sample_responses`**: Example user profiles for testing matching algorithms

### `values_matrix.csv`
Compatibility correlation matrix showing how different core values relate to each other.

**Purpose:**
- Each value represents how compatible two values are (0.0 to 1.0 scale)
- Higher scores = more compatible value combinations
- Used for advanced compatibility calculations (future enhancement)

## Survey Structure Details

### Basic Information (`basic_info`)
Collects fundamental demographic data:
- **Name**: User's display name
- **Age**: Must be 18-65 (legal family planning age range)
- **Location**: City/location for proximity matching

### Core Values (`values`)
8 values rated on 1-5 importance scale:
- **`family_first`**: Prioritizing family over other commitments
- **`career_balance`**: Work-life balance and career flexibility
- **`financial_security`**: Importance of financial stability
- **`emotional_intimacy`**: Value on emotional connection
- **`shared_parenting`**: Equal parenting responsibilities
- **`personal_growth`**: Individual development and growth
- **`community_involvement`**: Engagement with community
- **`spiritual_connection`**: Shared spiritual/religious beliefs

### Family Goals (`family_goals`)
Multiple selection options for family planning approaches:
- **`biological_children`**: Having biological children together
- **`adoption`**: Adopting children
- **`blended_family`**: Combining existing families
- **`single_parent_support`**: Supporting single parenting
- **`co_parenting`**: Shared parenting arrangements
- **`extended_family_close`**: Close extended family involvement

### Communication Styles (`communication`)
Single selection from 5 communication approaches:
- **`direct_honest`**: Straightforward, clear communication
- **`gentle_supportive`**: Caring, nurturing approach
- **`analytical_logical`**: Data-driven, rational discussion
- **`emotional_expressive`**: Open sharing of feelings
- **`collaborative_consensus`**: Group decision-making approach

### Timeline Preferences (`timeline`)
Single selection for family formation timing:
- **`within_1_year`**: Ready to start within 12 months
- **`1_to_3_years`**: Planning for 1-3 year timeframe
- **`3_to_5_years`**: Medium-term planning (3-5 years)
- **`5_plus_years`**: Long-term planning (5+ years)
- **`flexible_timing`**: Open to various timelines

## Sample User Profiles

### Demo User 1 (Alex)
- **Profile**: Career-focused with high emotional needs
- **Key Values**: Work-life balance (5), emotional intimacy (5), shared parenting (5)
- **Goals**: Biological children with shared parenting
- **Style**: Collaborative consensus building
- **Timeline**: 1-3 years

### Demo User 2 (Jordan)
- **Profile**: Family-first with spiritual emphasis
- **Key Values**: Family first (5), financial security (5), spiritual connection (5)
- **Goals**: Adoption with close extended family
- **Style**: Gentle and supportive
- **Timeline**: 3-5 years

## Data Relationships

### Model Synchronization
All data structures correspond to constants in `backend/models.py`:
- Survey values → `SurveyData.CORE_VALUES`
- Communication options → `SurveyData.COMMUNICATION_STYLES`
- Family goals → `SurveyData.FAMILY_GOALS`
- Timeline options → `SurveyData.TIMELINES`

### Dialogflow Integration
Entity definitions in `dialogflow_agent/agent.json` match these data structures:
- `@family_goals` entity uses `family_goals` options
- `@communication_style` entity uses `communication` options
- `@timeline` entity uses `timeline` options

## Usage in Application

### Development & Testing
- Load sample responses for algorithm testing
- Use survey structure for dynamic question generation
- Reference for frontend form building

### Production Considerations
- Survey structure could be loaded dynamically from database
- Sample responses serve as data format examples
- Values matrix enables sophisticated compatibility calculations

This data-driven approach ensures consistency across all application components and enables easy modification of survey questions and options.
