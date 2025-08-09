from models import CompatibilityScore

class ExplainabilityEngine:
    """
    Provides human-readable explanations for matching recommendations
    Critical for trust-building in family planning contexts
    """
    
    def explain_match(self, score: CompatibilityScore) -> dict:
        """Generate detailed explanation for a compatibility match"""
        
        explanation = {
            'overall_assessment': self._get_overall_assessment(score.overall_score),
            'strengths': self._identify_strengths(score),
            'considerations': self._identify_considerations(score),
            'detailed_breakdown': self._create_detailed_breakdown(score),
            'next_steps': self._suggest_next_steps(score)
        }
        
        return explanation
    
    def _get_overall_assessment(self, score: float) -> str:
        """Provide overall compatibility assessment"""
        if score >= 0.8:
            return "Excellent compatibility - This match shows strong potential for a successful family partnership."
        elif score >= 0.65:
            return "Good compatibility - This match shares important foundations with some areas to explore."
        elif score >= 0.5:
            return "Moderate compatibility - There are both shared elements and differences to consider."
        else:
            return "Lower compatibility - Significant differences may require careful consideration."
    
    def _identify_strengths(self, score: CompatibilityScore) -> list:
        """Identify the strongest compatibility areas"""
        strengths = []
        
        if score.values_score >= 0.7:
            strengths.append("Strong alignment on core life values")
        
        if score.goals_score >= 0.7:
            strengths.append("Shared vision for family structure and goals")
        
        if score.communication_score >= 0.7:
            strengths.append("Compatible communication and conflict resolution styles")
        
        if score.timeline_score >= 0.7:
            strengths.append("Aligned timeline for family planning")
        
        if not strengths:
            # Find the highest scoring area as a relative strength
            scores = {
                'values': score.values_score,
                'goals': score.goals_score,
                'communication': score.communication_score,
                'timeline': score.timeline_score
            }
            best_area = max(scores, key=scores.get)
            if scores[best_area] >= 0.5:
                area_names = {
                    'values': 'Some shared core values',
                    'goals': 'Some compatible family goals', 
                    'communication': 'Workable communication styles',
                    'timeline': 'Flexible timing compatibility'
                }
                strengths.append(area_names[best_area])
        
        return strengths
    
    def _identify_considerations(self, score: CompatibilityScore) -> list:
        """Identify areas that need attention or discussion"""
        considerations = []
        
        if score.values_score < 0.5:
            considerations.append("Different core values may require open discussion about priorities")
        
        if score.goals_score < 0.5:
            considerations.append("Different family goals would benefit from detailed exploration")
        
        if score.communication_score < 0.5:
            considerations.append("Communication style differences may need intentional bridge-building")
        
        if score.timeline_score < 0.5:
            considerations.append("Timeline misalignment requires honest conversation about expectations")
        
        return considerations
    
    def _create_detailed_breakdown(self, score: CompatibilityScore) -> dict:
        """Create detailed breakdown of each compatibility dimension"""
        return {
            'values_compatibility': {
                'score': score.values_score,
                'interpretation': self._interpret_score(score.values_score, 'values')
            },
            'family_goals_alignment': {
                'score': score.goals_score,
                'interpretation': self._interpret_score(score.goals_score, 'goals')
            },
            'communication_compatibility': {
                'score': score.communication_score,
                'interpretation': self._interpret_score(score.communication_score, 'communication')
            },
            'timeline_alignment': {
                'score': score.timeline_score,
                'interpretation': self._interpret_score(score.timeline_score, 'timeline')
            }
        }
    
    def _interpret_score(self, score: float, dimension: str) -> str:
        """Interpret individual dimension scores"""
        interpretations = {
            'values': {
                'high': "You both prioritize similar life values and principles",
                'medium': "You share some core values with room for complementary differences",
                'low': "Your value systems have notable differences that merit discussion"
            },
            'goals': {
                'high': "Your family planning goals are highly aligned",
                'medium': "You have overlapping family goals with some unique elements",
                'low': "Your family planning approaches differ significantly"
            },
            'communication': {
                'high': "Your communication styles complement each other well",
                'medium': "Your communication approaches can work together with some adaptation",
                'low': "Your communication styles may require extra effort to bridge"
            },
            'timeline': {
                'high': "Your family planning timelines align well",
                'medium': "Your timelines are compatible with some flexibility needed",
                'low': "Your preferred timelines have significant differences"
            }
        }
        
        if score >= 0.7:
            level = 'high'
        elif score >= 0.5:
            level = 'medium'
        else:
            level = 'low'
        
        return interpretations[dimension][level]
    
    def _suggest_next_steps(self, score: CompatibilityScore) -> list:
        """Suggest concrete next steps based on compatibility"""
        next_steps = []
        
        if score.overall_score >= 0.7:
            next_steps.extend([
                "Schedule a video call to explore your connection further",
                "Discuss your family planning timeline in detail",
                "Share more about your personal backgrounds and experiences"
            ])
        elif score.overall_score >= 0.5:
            next_steps.extend([
                "Have an honest conversation about your differences",
                "Explore areas of alignment more deeply",
                "Consider whether differences are complementary or conflicting"
            ])
        else:
            next_steps.extend([
                "Reflect on whether differences can be bridged",
                "Focus on finding common ground if you choose to connect",
                "Consider whether this match aligns with your priorities"
            ])
        
        # Add specific suggestions based on weak areas
        if score.values_score < 0.5:
            next_steps.append("Discuss core values and life priorities in depth")
        
        if score.communication_score < 0.5:
            next_steps.append("Explore how you each handle conflict and make decisions")
        
        return next_steps
    
    def generate_match_summary(self, scores: list) -> dict:
        """Generate summary of multiple matches for user dashboard"""
        if not scores:
            return {'message': 'No matches found. Consider expanding your criteria.'}
        
        avg_score = sum(s.overall_score for s in scores) / len(scores)
        top_score = max(s.overall_score for s in scores)
        
        summary = {
            'total_matches': len(scores),
            'average_compatibility': round(avg_score, 2),
            'best_match_score': round(top_score, 2),
            'recommendations': []
        }
        
        if top_score >= 0.8:
            summary['recommendations'].append("You have some excellent potential matches!")
        elif top_score >= 0.6:
            summary['recommendations'].append("You have several promising connections to explore.")
        else:
            summary['recommendations'].append("Consider expanding your search criteria or location range.")
        
        return summary
