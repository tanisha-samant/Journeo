from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.models.trip import Trip
from app.schemas.trip import TripCreate, TripResponse, ItineraryRequest
from app.services.ai_service import AIService
from app.services.weather_service import WeatherService
from app.services.currency_service import CurrencyService
from app.services.translation_service import TranslationService

router = APIRouter(prefix="/api/trips", tags=["trips"])

ai_service = AIService()
weather_service = WeatherService()
currency_service = CurrencyService()
translation_service = TranslationService()


@router.post("/plan", response_model=dict)
async def plan_trip(request: ItineraryRequest, db: Session = Depends(get_db)):
    """
    Generate an AI-powered travel itinerary
    """
    try:
        # Generate itinerary using AI
        trip_data = {
            "source": request.source,
            "destination": request.destination,
            "start_date": request.start_date,
            "end_date": request.end_date,
            "budget": request.budget,
            "travel_type": request.travel_type,
            "preferences": request.preferences
        }
        
        itinerary = ai_service.generate_itinerary(trip_data)
        
        # Get weather information for destination
        weather = weather_service.get_current_weather(request.destination)
        forecast = weather_service.get_forecast(request.destination)
        
        # Get currency information if budget is provided
        currency_info = None
        if request.budget:
            currency_info = currency_service.get_exchange_rates("USD")
        
        # Translate itinerary if language is specified
        translated_itinerary = None
        if request.language and request.language != "en":
            translation_result = translation_service.translate_itinerary(itinerary, request.language)
            if translation_result["success"]:
                translated_itinerary = translation_result["translated_itinerary"]
        
        # Save trip to database
        db_trip = Trip(
            source=request.source,
            destination=request.destination,
            start_date=request.start_date,
            end_date=request.end_date,
            budget=request.budget,
            travel_type=request.travel_type,
            preferences=request.preferences,
            itinerary=itinerary
        )
        
        db.add(db_trip)
        db.commit()
        db.refresh(db_trip)
        
        return {
            "trip_id": db_trip.id,
            "itinerary": itinerary,
            "translated_itinerary": translated_itinerary,
            "weather": weather,
            "forecast": forecast,
            "currency_info": currency_info,
            "success": True
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error planning trip: {str(e)}")


@router.get("/", response_model=List[TripResponse])
async def get_trips(db: Session = Depends(get_db)):
    """
    Get all trips
    """
    trips = db.query(Trip).all()
    return trips


@router.get("/{trip_id}", response_model=TripResponse)
async def get_trip(trip_id: int, db: Session = Depends(get_db)):
    """
    Get a specific trip by ID
    """
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.delete("/{trip_id}")
async def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    """
    Delete a trip
    """
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    db.delete(trip)
    db.commit()
    
    return {"message": "Trip deleted successfully"} 