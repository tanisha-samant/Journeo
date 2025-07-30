from fastapi import APIRouter, HTTPException
from app.schemas.trip import WeatherRequest
from app.services.weather_service import WeatherService

router = APIRouter(prefix="/api/weather", tags=["weather"])

weather_service = WeatherService()


@router.get("/{city}")
async def get_weather(city: str, country_code: str = None):
    """
    Get current weather for a city
    """
    try:
        weather = weather_service.get_current_weather(city, country_code)
        return weather
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching weather: {str(e)}")


@router.get("/{city}/forecast")
async def get_forecast(city: str, country_code: str = None):
    """
    Get weather forecast for a city
    """
    try:
        forecast = weather_service.get_forecast(city, country_code)
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching forecast: {str(e)}")


@router.post("/")
async def get_weather_by_request(request: WeatherRequest):
    """
    Get weather information using request body
    """
    try:
        weather = weather_service.get_current_weather(request.city, request.country_code)
        forecast = weather_service.get_forecast(request.city, request.country_code)
        
        return {
            "current": weather,
            "forecast": forecast
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}") 