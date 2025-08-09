from dataclasses import dataclass
from typing import List, Dict, Optional
import json

@dataclass
class UserProfile:
    """User profile model for compatibility matching"""
    user_id: str
    name: str
    age: int
    location: str
    values: Dict[str, int]  # Values with importance scores (1-5)
    preferences: Dict[str, any]
    communication_style: str
    family_goals: List[str]
    timeline: str
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'age': self.age,
            'location': self.location,
            'values': self.values,
            'preferences': self.preferences,
            'communication_style': self.communication_style,
            'family_goals': self.family_goals,
            'timeline': self.timeline
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

@dataclass
class CompatibilityScore:
    """Compatibility score between two users"""
    user1_id: str
    user2_id: str
    overall_score: float
    values_score: float
    goals_score: float
    communication_score: float
    timeline_score: float
    explanation: str
    
class SurveyData:
    """Survey data structure for collecting user information"""
    
    CORE_VALUES = [
        "family_first",
        "career_balance", 
        "financial_security",
        "emotional_intimacy",
        "shared_parenting",
        "personal_growth",
        "community_involvement",
        "spiritual_connection"
    ]
    
    COMMUNICATION_STYLES = [
        "direct_honest",
        "gentle_supportive", 
        "analytical_logical",
        "emotional_expressive",
        "collaborative_consensus"
    ]
    
    FAMILY_GOALS = [
        "biological_children",
        "adoption",
        "blended_family",
        "single_parent_support",
        "co_parenting",
        "extended_family_close"
    ]
    
    TIMELINES = [
        "within_1_year",
        "1_to_3_years", 
        "3_to_5_years",
        "5_plus_years",
        "flexible_timing"
    ]
