import os
from crewai import Agent, Task, Crew, Process
from groq import Groq
from app.config import settings
from typing import Dict, Any


class AIService:
    def __init__(self):
        self.client = Groq(api_key=settings.groq_api_key)
        
    def generate_itinerary(self, trip_data: Dict[str, Any]) -> str:
        """
        Generate a personalized travel itinerary using CrewAI and Groq
        """
        try:
            # Create agents for different aspects of trip planning
            travel_researcher = Agent(
                role='Travel Research Specialist',
                goal='Research the best attractions, activities, and local insights for the destination',
                backstory="""You are an expert travel researcher with years of experience 
                in discovering hidden gems and must-visit places in cities around the world. 
                You know how to find authentic local experiences and tourist attractions.""",
                verbose=True,
                allow_delegation=False,
                llm=self.client
            )
            
            itinerary_planner = Agent(
                role='Itinerary Planner',
                goal='Create detailed, well-structured daily itineraries that optimize time and experience',
                backstory="""You are a professional itinerary planner who excels at creating 
                logical, enjoyable travel schedules. You understand how to balance activities, 
                rest, and travel time to create the perfect trip experience.""",
                verbose=True,
                allow_delegation=False,
                llm=self.client
            )
            
            budget_advisor = Agent(
                role='Budget Travel Advisor',
                goal='Provide cost-effective travel options and budget-friendly recommendations',
                backstory="""You are a budget travel expert who knows how to maximize 
                travel experiences while minimizing costs. You can suggest affordable 
                alternatives and money-saving tips.""",
                verbose=True,
                allow_delegation=False,
                llm=self.client
            )
            
            # Create tasks for the crew
            research_task = Task(
                description=f"""
                Research the destination: {trip_data['destination']}
                
                Focus on:
                - Top attractions and landmarks
                - Local culture and customs
                - Best times to visit places
                - Local cuisine and restaurants
                - Transportation options
                - Safety considerations
                
                Trip details:
                - Duration: {trip_data['start_date']} to {trip_data['end_date']}
                - Budget: {trip_data.get('budget', 'Not specified')}
                - Travel type: {trip_data.get('travel_type', 'General')}
                - Preferences: {trip_data.get('preferences', 'None specified')}
                
                Provide comprehensive research findings that will help create the best itinerary.
                """,
                agent=travel_researcher
            )
            
            planning_task = Task(
                description=f"""
                Create a detailed daily itinerary based on the research findings.
                
                Requirements:
                - Create day-by-day schedule
                - Include specific times for activities
                - Consider travel time between locations
                - Balance sightseeing with rest
                - Include meal recommendations
                - Suggest transportation methods
                - Account for weather and seasonal factors
                
                Make the itinerary engaging, realistic, and tailored to the traveler's preferences.
                """,
                agent=itinerary_planner
            )
            
            budget_task = Task(
                description=f"""
                Review the itinerary and provide budget-friendly alternatives and cost estimates.
                
                Tasks:
                - Estimate costs for each activity
                - Suggest budget-friendly alternatives
                - Provide money-saving tips
                - Recommend affordable dining options
                - Suggest cost-effective transportation
                
                Ensure the trip fits within the specified budget while maintaining quality experiences.
                """,
                agent=budget_advisor
            )
            
            # Create and run the crew
            crew = Crew(
                agents=[travel_researcher, itinerary_planner, budget_advisor],
                tasks=[research_task, planning_task, budget_task],
                verbose=True,
                process=Process.sequential
            )
            
            result = crew.kickoff()
            
            return result
            
        except Exception as e:
            # Fallback to a simple itinerary if AI service fails
            return self._generate_fallback_itinerary(trip_data)
    
    def _generate_fallback_itinerary(self, trip_data: Dict[str, Any]) -> str:
        """
        Generate a simple fallback itinerary when AI service is unavailable
        """
        destination = trip_data['destination']
        start_date = trip_data['start_date']
        end_date = trip_data['end_date']
        
        return f"""
        # Travel Itinerary for {destination}
        
        **Trip Details:**
        - Destination: {destination}
        - Start Date: {start_date}
        - End Date: {end_date}
        - Budget: {trip_data.get('budget', 'Not specified')}
        
        **Day 1 - Arrival and Orientation:**
        - Arrive in {destination}
        - Check into accommodation
        - Take a walking tour of the city center
        - Visit local landmarks
        - Enjoy dinner at a local restaurant
        
        **Day 2 - Cultural Exploration:**
        - Visit museums and cultural sites
        - Explore local markets
        - Try traditional cuisine
        - Evening entertainment (theater, music, etc.)
        
        **Day 3 - Nature and Adventure:**
        - Outdoor activities or nature walks
        - Visit parks or natural attractions
        - Shopping for souvenirs
        - Farewell dinner
        
        **Tips:**
        - Research local customs and etiquette
        - Learn basic phrases in the local language
        - Keep emergency contacts handy
        - Stay hydrated and well-rested
        
        *Note: This is a basic itinerary. For a more personalized experience, please ensure all API keys are properly configured.*
        """ 