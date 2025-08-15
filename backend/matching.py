"""
Compatibility matching engine for family planning partnerships

Implements rule-based algorithms to calculate compatibility scores
between users based on values, goals, communication styles, and timelines.
Uses weighted scoring for explainable AI recommendations.
"""

import numpy as np
import pandas as pd
from typing import List, Tuple
from models import UserProfile, CompatibilityScore

class CompatibilityEngine:
    """
    Main compatibility calculation engine
    
    Calculates multi-dimensional compatibility scores between users
    using weighted factors: values (35%), goals (30%), 
    communication (20%), and timeline (15%).
    """
    
    def __init__(self):
        """Initialize the engine with scoring weights"""
        # Weights for different compatibility factors (must sum to 1.0)
        self.weights = {
            'values': 0.35,        # Values alignment weight
            'goals': 0.30,         # Family goals compatibility weight
            'communication': 0.20, # Communication style match weight
            'timeline': 0.15       # Timeline alignment weight
        }
    
    def calculate_compatibility(self, user1: UserProfile, user2: UserProfile) -> CompatibilityScore:
        """
        Calculate comprehensive compatibility score between two users
        
        Args:
            user1: First user's profile
            user2: Second user's profile
            
        Returns:
            CompatibilityScore object with overall score and breakdown
        """
        
        # Calculate individual dimension scores
        values_score = self._calculate_values_score(user1, user2)
        goals_score = self._calculate_goals_score(user1, user2)
        communication_score = self._calculate_communication_score(user1, user2)
        timeline_score = self._calculate_timeline_score(user1, user2)
        
        # Weighted overall score
        overall_score = (
            values_score * self.weights['values'] +
            goals_score * self.weights['goals'] +
            communication_score * self.weights['communication'] +
            timeline_score * self.weights['timeline']
        )
        
        explanation = self._generate_explanation(
            values_score, goals_score, communication_score, timeline_score
        )
        
        return CompatibilityScore(
            user1_id=user1.user_id,
            user2_id=user2.user_id,
            overall_score=round(overall_score, 2),
            values_score=round(values_score, 2),
            goals_score=round(goals_score, 2),
            communication_score=round(communication_score, 2),
            timeline_score=round(timeline_score, 2),
            explanation=explanation
        )
    
    def _calculate_values_score(self, user1: UserProfile, user2: UserProfile) -> float:
        """Calculate compatibility based on shared values"""
        if not user1.values or not user2.values:
            return 0.5
        
        # Find common values and calculate alignment
        common_values = set(user1.values.keys()) & set(user2.values.keys())
        if not common_values:
            return 0.3
        
        alignment_scores = []
        for value in common_values:
            # Score based on how close their importance ratings are
            diff = abs(user1.values[value] - user2.values[value])
            alignment = 1 - (diff / 4)  # Max diff is 4 (5-1), so normalize
            alignment_scores.append(alignment)
        
        return np.mean(alignment_scores)
    
    def _calculate_goals_score(self, user1: UserProfile, user2: UserProfile) -> float:
        """Calculate compatibility based on family goals"""
        if not user1.family_goals or not user2.family_goals:
            return 0.5
        
        # Calculate overlap in family goals
        goals1 = set(user1.family_goals)
        goals2 = set(user2.family_goals)
        
        overlap = len(goals1 & goals2)
        total_unique = len(goals1 | goals2)
        
        if total_unique == 0:
            return 0.5
        
        return overlap / total_unique
    
    def _calculate_communication_score(self, user1: UserProfile, user2: UserProfile) -> float:
        """Calculate compatibility based on communication styles"""
        if user1.communication_style == user2.communication_style:
            return 1.0
        
        # Define compatible communication style pairs
        compatible_pairs = {
            ('direct_honest', 'analytical_logical'): 0.8,
            ('gentle_supportive', 'emotional_expressive'): 0.8,
            ('collaborative_consensus', 'gentle_supportive'): 0.7,
            ('direct_honest', 'collaborative_consensus'): 0.6,
            ('analytical_logical', 'collaborative_consensus'): 0.6
        }
        
        pair = (user1.communication_style, user2.communication_style)
        reverse_pair = (user2.communication_style, user1.communication_style)
        
        return compatible_pairs.get(pair, compatible_pairs.get(reverse_pair, 0.4))
    
    def _calculate_timeline_score(self, user1: UserProfile, user2: UserProfile) -> float:
        """Calculate compatibility based on family planning timeline"""
        timeline_order = [
            "within_1_year",
            "1_to_3_years", 
            "3_to_5_years",
            "5_plus_years",
            "flexible_timing"
        ]
        
        try:
            idx1 = timeline_order.index(user1.timeline)
            idx2 = timeline_order.index(user2.timeline)
            
            # Flexible timing is compatible with everything
            if user1.timeline == "flexible_timing" or user2.timeline == "flexible_timing":
                return 0.9
            
            # Calculate score based on timeline proximity
            diff = abs(idx1 - idx2)
            return max(0.2, 1 - (diff * 0.3))
            
        except ValueError:
            return 0.5
    
    def _generate_explanation(self, values_score, goals_score, communication_score, timeline_score) -> str:
        """Generate human-readable explanation of compatibility"""
        explanations = []
        
        if values_score >= 0.7:
            explanations.append("Strong alignment on core values")
        elif values_score >= 0.5:
            explanations.append("Moderate values compatibility") 
        else:
            explanations.append("Different value priorities")
        
        if goals_score >= 0.7:
            explanations.append("highly compatible family goals")
        elif goals_score >= 0.5:
            explanations.append("some shared family aspirations")
        else:
            explanations.append("different family planning approaches")
        
        if communication_score >= 0.7:
            explanations.append("complementary communication styles")
        elif communication_score >= 0.5:
            explanations.append("workable communication differences")
        else:
            explanations.append("potentially challenging communication dynamics")
        
        if timeline_score >= 0.7:
            explanations.append("aligned timing preferences")
        else:
            explanations.append("different timeline expectations")
        
        return "; ".join(explanations) + "."
    
    def find_top_matches(self, user: UserProfile, candidates: List[UserProfile], top_n=5) -> List[CompatibilityScore]:
        """Find top N compatible matches for a user"""
        scores = []
        
        for candidate in candidates:
            if candidate.user_id != user.user_id:
                score = self.calculate_compatibility(user, candidate)
                scores.append(score)
        
        # Sort by overall score descending
        scores.sort(key=lambda x: x.overall_score, reverse=True)
        return scores[:top_n]
