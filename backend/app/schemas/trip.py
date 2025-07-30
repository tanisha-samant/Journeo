from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class TripBase(BaseModel):
    source: str
    destination: str
    start_date: datetime
    end_date: datetime
    budget: Optional[float] = None
    travel_type: Optional[str] = None
    preferences: Optional[Dict[str, Any]] = None


class TripCreate(TripBase):
    pass


class TripResponse(TripBase):
    id: int
    itinerary: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class ItineraryRequest(BaseModel):
    source: str
    destination: str
    start_date: datetime
    end_date: datetime
    budget: Optional[float] = None
    travel_type: Optional[str] = None
    preferences: Optional[Dict[str, Any]] = None
    language: Optional[str] = "en"


class WeatherRequest(BaseModel):
    city: str
    country_code: Optional[str] = None


class RouteRequest(BaseModel):
    start: str
    end: str
    mode: str = "driving"  # driving, walking, cycling, transit


class CurrencyRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: float = 1.0


class TranslationRequest(BaseModel):
    text: str
    target_language: str
    source_language: Optional[str] = "auto" 