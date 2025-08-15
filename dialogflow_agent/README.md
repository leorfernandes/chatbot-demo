# Dialogflow Agent Configuration

This document explains the structure and purpose of the `agent.json` file, which contains the complete Dialogflow agent configuration for the compatibility chatbot.

## Agent Overview

**Name:** `compatibility-chatbot-demo`
**Purpose:** AI-powered compatibility chatbot for intentional family planning
**Language:** English (en)

## Webhook Configuration

```json
"webhook": {
  "url": "https://your-backend-url.com/webhook",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

**Purpose:** All intents with `"webhook": true` will send requests to this URL for processing by the Python backend.

## Intent Definitions

### 1. Welcome Intent (`welcome`)
**Purpose:** Initiates conversation and welcomes users
**Training Phrases:** 
- Greeting variations: "hello", "hi", "hey"
- Action requests: "start", "begin", "let's start"
- Specific requests: "I want to find matches"

**Webhook:** ✅ Enabled - Routes to `handle_welcome()` in backend

### 2. Basic Info Collection (`collect.basic.info`)
**Purpose:** Captures user's name, age, and location
**Training Phrases:**
- Name patterns: "My name is John", "I'm Sarah", "Call me Alex"
- Age patterns: "I am 30 years old", "I'm 25", "My age is 32"
- Location patterns: "I live in Seattle", "I'm from New York"

**Parameters:**
- `person` - Uses `@sys.person` system entity for name extraction
- `age` - Uses `@sys.age` system entity for age extraction  
- `location` - Uses `@sys.location` system entity for location extraction

**Webhook:** ✅ Enabled - Routes to `handle_basic_info()` in backend

### 3. Values Collection (`collect.values`)
**Purpose:** Collects importance ratings (1-5) for core values
**Training Phrases:**
- Numeric: "5", "4 out of 5", "1", "2", "3"
- Descriptive: "very important", "extremely important", "not important"

**Parameters:**
- `number` - Uses `@sys.number` system entity to extract rating values

**Webhook:** ✅ Enabled - Routes to `handle_values()` in backend

### 4. Family Goals Collection (`collect.family.goals`)
**Purpose:** Captures family planning goals and preferences
**Training Phrases:**
- Goal statements: "I want biological children", "adoption is important to me"
- Multiple goals: "biological children and adoption"
- Specific approaches: "blended family", "co-parenting"

**Parameters:**
- `family-goals` - Uses custom `@family_goals` entity (list enabled for multiple selections)

**Webhook:** ✅ Enabled - Routes to `handle_family_goals()` in backend

### 5. Communication Style (`collect.communication.style`)
**Purpose:** Identifies user's preferred communication approach
**Training Phrases:**
- Direct style: "I'm direct and honest", "I'm more analytical"
- Supportive style: "gentle and supportive", "I'm gentle in my approach"
- Collaborative: "collaborative", "I prefer consensus building"

**Parameters:**
- `communication-style` - Uses custom `@communication_style` entity

**Webhook:** ✅ Enabled - Routes to `handle_communication_style()` in backend

### 6. Timeline Collection (`collect.timeline`)
**Purpose:** Determines preferred timeline for family formation
**Training Phrases:**
- Specific timings: "within 1 year", "1 to 3 years", "3 to 5 years"
- Flexible options: "I'm flexible", "not sure about timing"
- Relative terms: "soon", "in a few years"

**Parameters:**
- `timeline` - Uses custom `@timeline` entity

**Webhook:** ✅ Enabled - Routes to `handle_timeline()` in backend

### 7. Find Matches (`find.matches`)
**Purpose:** Triggers compatibility matching process
**Training Phrases:**
- Direct requests: "find matches", "show me matches"
- Affirmative responses: "yes find matches", "let's find matches"
- Action statements: "I want to see my matches"

**Parameters:** None required

**Webhook:** ✅ Enabled - Routes to `handle_find_matches()` in backend

### 8. Explain Match (`explain.match`)
**Purpose:** Provides detailed explanations for specific matches
**Training Phrases:**
- General requests: "explain this match", "why is this a good match"
- Specific requests: "explain the first match", "tell me more about this match"
- Reasoning requests: "why did you recommend this"

**Parameters:**
- `match-number` - Uses `@sys.number` to identify which match to explain

**Webhook:** ✅ Enabled - Routes to `handle_explain_match()` in backend

## Custom Entity Definitions

### 1. Family Goals Entity (`@family_goals`)
**Purpose:** Structured extraction of family planning goals

**Values and Synonyms:**
- `biological_children`: "biological children", "bio children", "having children", "natural children"
- `adoption`: "adopt", "adopting", "adopted children"
- `blended_family`: "blended family", "step children", "bringing families together"
- `co_parenting`: "co-parenting", "shared parenting", "co parenting"
- `single_parent_support`: "single parent", "single parenting", "solo parenting"
- `extended_family_close`: "extended family", "close family", "family closeness"

### 2. Communication Style Entity (`@communication_style`)
**Purpose:** Identification of communication preferences

**Values and Synonyms:**
- `direct_honest`: "direct", "honest", "straightforward", "blunt"
- `gentle_supportive`: "gentle", "supportive", "kind", "nurturing"
- `analytical_logical`: "analytical", "logical", "rational", "methodical"
- `emotional_expressive`: "emotional", "expressive", "feelings-focused", "heart-centered"
- `collaborative_consensus`: "collaborative", "consensus", "team-oriented", "democratic"

### 3. Timeline Entity (`@timeline`)
**Purpose:** Timeline preference extraction

**Values and Synonyms:**
- `within_1_year`: "within 1 year", "within a year", "soon", "immediately", "asap"
- `1_to_3_years`: "1 to 3 years", "1-3 years", "couple years", "2-3 years"
- `3_to_5_years`: "3 to 5 years", "3-5 years", "few years", "4-5 years"
- `5_plus_years`: "5 plus years", "5+ years", "many years", "long term"
- `flexible_timing`: "flexible", "open", "not sure", "depends", "variable"

## Webhook Integration Flow

1. **User Input** → Dialogflow processes and identifies intent
2. **Entity Extraction** → Dialogflow extracts relevant parameters
3. **Webhook Request** → Dialogflow sends structured data to Python backend
4. **Backend Processing** → Python handles business logic and data storage
5. **Response Generation** → Backend returns appropriate response text
6. **User Display** → Dialogflow shows the response to user

## Training Considerations

### Natural Language Variations
Each intent includes multiple phrasings to handle natural conversation variations. The training phrases cover:
- Formal vs. informal language
- Different ways to express the same concept
- Common variations in user responses

### Entity Recognition
Custom entities use synonym lists to handle:
- Alternative terms for the same concept
- Common abbreviations and slang
- Regional language variations

### Conversation Flow
Intents are designed to support a linear conversation flow while allowing for:
- User corrections and clarifications
- Non-linear conversation patterns
- Fallback to previous steps if needed

This configuration enables natural, flowing conversations while maintaining structured data collection for the compatibility matching algorithms.
