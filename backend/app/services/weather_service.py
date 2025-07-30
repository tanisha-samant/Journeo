import requests
from typing import Dict, Any, Optional
from app.config import settings


class WeatherService:
    def __init__(self):
        self.api_key = settings.openweather_api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        
    def get_current_weather(self, city: str, country_code: Optional[str] = None) -> Dict[str, Any]:
        """
        Get current weather for a city
        """
        try:
            location = f"{city},{country_code}" if country_code else city
            url = f"{self.base_url}/weather"
            params = {
                "q": location,
                "appid": self.api_key,
                "units": "metric"  # Use Celsius
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "wind_speed": data["wind"]["speed"],
                "wind_direction": data["wind"].get("deg", 0),
                "visibility": data.get("visibility", 0),
                "sunrise": data["sys"]["sunrise"],
                "sunset": data["sys"]["sunset"]
            }
            
        except requests.RequestException as e:
            return self._get_mock_weather(city)
    
    def get_forecast(self, city: str, country_code: Optional[str] = None) -> Dict[str, Any]:
        """
        Get 5-day weather forecast for a city
        """
        try:
            location = f"{city},{country_code}" if country_code else city
            url = f"{self.base_url}/forecast"
            params = {
                "q": location,
                "appid": self.api_key,
                "units": "metric"
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            # Process forecast data
            forecast = []
            for item in data["list"]:
                forecast.append({
                    "datetime": item["dt"],
                    "temperature": item["main"]["temp"],
                    "feels_like": item["main"]["feels_like"],
                    "humidity": item["main"]["humidity"],
                    "description": item["weather"][0]["description"],
                    "icon": item["weather"][0]["icon"],
                    "wind_speed": item["wind"]["speed"],
                    "pop": item.get("pop", 0)  # Probability of precipitation
                })
            
            return {
                "city": data["city"]["name"],
                "country": data["city"]["country"],
                "forecast": forecast
            }
            
        except requests.RequestException as e:
            return self._get_mock_forecast(city)
    
    def _get_mock_weather(self, city: str) -> Dict[str, Any]:
        """
        Return mock weather data when API is unavailable
        """
        return {
            "city": city,
            "country": "Unknown",
            "temperature": 22.5,
            "feels_like": 24.0,
            "humidity": 65,
            "pressure": 1013,
            "description": "partly cloudy",
            "icon": "02d",
            "wind_speed": 3.2,
            "wind_direction": 180,
            "visibility": 10000,
            "sunrise": 1640995200,
            "sunset": 1641038400
        }
    
    def _get_mock_forecast(self, city: str) -> Dict[str, Any]:
        """
        Return mock forecast data when API is unavailable
        """
        import time
        current_time = int(time.time())
        
        forecast = []
        for i in range(40):  # 5 days * 8 forecasts per day
            forecast.append({
                "datetime": current_time + (i * 10800),  # 3 hours apart
                "temperature": 20 + (i % 10),  # Varying temperature
                "feels_like": 22 + (i % 8),
                "humidity": 60 + (i % 20),
                "description": "partly cloudy",
                "icon": "02d",
                "wind_speed": 2.5 + (i % 3),
                "pop": 0.1 + (i % 5) * 0.1
            })
        
        return {
            "city": city,
            "country": "Unknown",
            "forecast": forecast
        } 