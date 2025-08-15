"""
Data models for the family planning compatibility chatbot

Contains user profiles, compatibility scores, and survey data structures
used throughout the matching and explanation system.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import json

@dataclass
class UserProfile:
    """
    Represents a user's complete profile for compatibility matching
    
    Stores all collected information including personal details,
    values, preferences, and family planning goals.
    """
    user_id: str                    # Unique identifier for this user
    name: str                       # User's display name
    age: int                        # User's age in years
    location: str                   # User's city/location
    values: Dict[str, int]         # Values with importance scores (1-5)
    preferences: Dict[str, Any]     # General preferences and settings
    communication_style: str       # Preferred communication approach
    family_goals: List[str]        # List of family planning goals
    timeline: str                  # Preferred timeline for family formation
    
    def to_dict(self):
        """Convert profile to dictionary for JSON serialization"""
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
        """Create UserProfile instance from dictionary data"""
        return cls(**data)

@dataclass
class CompatibilityScore:
    """
    Represents compatibility analysis between two users
    
    Contains overall score and breakdown by different compatibility
    dimensions, plus human-readable explanation.
    """
    user1_id: str           # First user's identifier
    user2_id: str           # Second user's identifier
    overall_score: float    # Combined compatibility score (0.0-1.0)
    values_score: float     # Values alignment score (0.0-1.0)
    goals_score: float      # Family goals compatibility (0.0-1.0)
    communication_score: float  # Communication style match (0.0-1.0)
    timeline_score: float   # Timeline alignment score (0.0-1.0)
    explanation: str        # Human-readable explanation of the match
    
class SurveyData:
    """
    Static data structure containing survey options and categories
    
    Defines all possible values for user profile fields used in
    the compatibility matching system.
    """
    
    # Core values that users rate on importance (1-5 scale)
    CORE_VALUES = [
        "family_first",         # Prioritizing family over other commitments
        "career_balance",       # Balancing career with family life
        "financial_security",   # Importance of financial stability
        "emotional_intimacy",   # Value on emotional connection
        "shared_parenting",     # Equal parenting responsibilities
        "personal_growth",      # Individual development and growth
        "community_involvement", # Engagement with community
        "spiritual_connection"  # Shared spiritual/religious beliefs
    ]
    
    # Different communication approaches people prefer
    COMMUNICATION_STYLES = [
        "direct_honest",        # Straightforward, clear communication
        "gentle_supportive",    # Caring, nurturing approach
        "analytical_logical",   # Data-driven, rational discussion
        "emotional_expressive", # Open sharing of feelings
        "collaborative_consensus" # Group decision-making approach
    ]
    
    # Various family formation goals users can select
    FAMILY_GOALS = [
        "biological_children",   # Having biological children together
        "adoption",             # Adopting children
        "blended_family",       # Combining existing families
        "single_parent_support", # Supporting single parenting
        "co_parenting",         # Shared parenting arrangements
        "extended_family_close" # Close extended family involvement
    ]
    
    # Timeline preferences for starting family formation
    TIMELINES = [
        "within_1_year",    # Ready to start within 12 months
        "1_to_3_years",     # Planning for 1-3 year timeframe
        "3_to_5_years",     # Medium-term planning (3-5 years)
        "5_plus_years",     # Long-term planning (5+ years)
        "flexible_timing"   # Open to various timelines
    ]
