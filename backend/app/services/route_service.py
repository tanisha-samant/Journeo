import requests
from typing import Dict, Any, Optional, List
from app.config import settings


class RouteService:
    def __init__(self):
        self.api_key = settings.openroute_api_key
        self.base_url = "https://api.openrouteservice.org/v2"
        
    def get_route(self, start: str, end: str, mode: str = "driving") -> Dict[str, Any]:
        """
        Get route between two points using OpenRouteService API
        """
        try:
            # First, geocode the addresses to get coordinates
            start_coords = self._geocode_address(start)
            end_coords = self._geocode_address(end)
            
            if not start_coords or not end_coords:
                return self._get_mock_route(start, end, mode)
            
            # Map mode to OpenRouteService profile
            profile_map = {
                "driving": "driving-car",
                "walking": "foot-walking",
                "cycling": "cycling-regular",
                "transit": "driving-car"  # OpenRouteService doesn't have transit, using driving as fallback
            }
            
            profile = profile_map.get(mode, "driving-car")
            
            url = f"{self.base_url}/directions/{profile}/geojson"
            
            payload = {
                "coordinates": [
                    [start_coords["lon"], start_coords["lat"]],
                    [end_coords["lon"], end_coords["lat"]]
                ],
                "instructions": True,
                "preference": "fastest",
                "units": "km"
            }
            
            headers = {
                "Authorization": self.api_key,
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            # Process the route data
            route = data["features"][0]
            properties = route["properties"]
            geometry = route["geometry"]
            
            return {
                "start": start,
                "end": end,
                "mode": mode,
                "distance": properties["segments"][0]["distance"] / 1000,  # Convert to km
                "duration": properties["segments"][0]["duration"] / 60,  # Convert to minutes
                "coordinates": geometry["coordinates"],
                "instructions": self._process_instructions(properties["segments"][0]["steps"]),
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_route(start, end, mode)
    
    def get_multimodal_route(self, start: str, end: str) -> Dict[str, Any]:
        """
        Get multimodal route suggestions (combining different transport modes)
        """
        try:
            routes = {}
            
            # Get routes for different modes
            for mode in ["driving", "walking", "cycling"]:
                route = self.get_route(start, end, mode)
                if route["success"]:
                    routes[mode] = route
            
            return {
                "start": start,
                "end": end,
                "routes": routes,
                "success": True
            }
            
        except Exception as e:
            return self._get_mock_multimodal_route(start, end)
    
    def _geocode_address(self, address: str) -> Optional[Dict[str, float]]:
        """
        Geocode an address to get coordinates
        """
        try:
            url = "https://api.openrouteservice.org/geocode/search"
            params = {
                "text": address,
                "size": 1
            }
            
            headers = {
                "Authorization": self.api_key
            }
            
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            if data["features"]:
                feature = data["features"][0]
                return {
                    "lat": feature["geometry"]["coordinates"][1],
                    "lon": feature["geometry"]["coordinates"][0]
                }
            
            return None
            
        except requests.RequestException:
            return None
    
    def _process_instructions(self, steps: List[Dict]) -> List[Dict]:
        """
        Process route instructions into a more readable format
        """
        instructions = []
        
        for step in steps:
            instructions.append({
                "instruction": step["instruction"],
                "distance": step["distance"],
                "duration": step["duration"],
                "type": step.get("type", "unknown")
            })
        
        return instructions
    
    def _get_mock_route(self, start: str, end: str, mode: str) -> Dict[str, Any]:
        """
        Return mock route data when API is unavailable
        """
        # Mock distances and durations based on mode
        mock_data = {
            "driving": {"distance": 15.5, "duration": 25},
            "walking": {"distance": 2.1, "duration": 30},
            "cycling": {"distance": 2.1, "duration": 12},
            "transit": {"distance": 15.5, "duration": 35}
        }
        
        data = mock_data.get(mode, mock_data["driving"])
        
        return {
            "start": start,
            "end": end,
            "mode": mode,
            "distance": data["distance"],
            "duration": data["duration"],
            "coordinates": [
                [-74.006, 40.7128],  # Mock coordinates
                [-73.935242, 40.730610]
            ],
            "instructions": [
                {
                    "instruction": f"Start from {start}",
                    "distance": 0,
                    "duration": 0,
                    "type": "start"
                },
                {
                    "instruction": f"Travel to {end}",
                    "distance": data["distance"],
                    "duration": data["duration"],
                    "type": "travel"
                }
            ],
            "success": True
        }
    
    def _get_mock_multimodal_route(self, start: str, end: str) -> Dict[str, Any]:
        """
        Return mock multimodal route data when API is unavailable
        """
        routes = {}
        
        for mode in ["driving", "walking", "cycling"]:
            routes[mode] = self._get_mock_route(start, end, mode)
        
        return {
            "start": start,
            "end": end,
            "routes": routes,
            "success": True
        } 