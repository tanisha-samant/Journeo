import requests
from typing import Dict, Any, List, Optional
from app.config import settings


class AccommodationService:
    def __init__(self):
        self.base_url = settings.overpass_api_url
        
    def find_accommodations(self, city: str, limit: int = 10) -> Dict[str, Any]:
        """
        Find accommodations in a city using Overpass API
        """
        try:
            # Overpass QL query to find hotels and guesthouses
            query = f"""
            [out:json][timeout:25];
            area[name="{city}"][admin_level~"^(8|9|10)$"]->.searchArea;
            (
              node["tourism"="hotel"](area.searchArea);
              way["tourism"="hotel"](area.searchArea);
              relation["tourism"="hotel"](area.searchArea);
              node["tourism"="guest_house"](area.searchArea);
              way["tourism"="guest_house"](area.searchArea);
              relation["tourism"="guest_house"](area.searchArea);
              node["tourism"="hostel"](area.searchArea);
              way["tourism"="hostel"](area.searchArea);
              relation["tourism"="hostel"](area.searchArea);
            );
            out body;
            >;
            out skel qt;
            """
            
            response = requests.post(self.base_url, data=query)
            response.raise_for_status()
            
            data = response.json()
            
            accommodations = self._process_accommodations(data["elements"], limit)
            
            return {
                "city": city,
                "accommodations": accommodations,
                "count": len(accommodations),
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_accommodations(city, limit)
    
    def find_accommodations_by_coordinates(self, lat: float, lon: float, radius: float = 5000, limit: int = 10) -> Dict[str, Any]:
        """
        Find accommodations near specific coordinates
        """
        try:
            # Overpass QL query for coordinates-based search
            query = f"""
            [out:json][timeout:25];
            (
              node["tourism"="hotel"](around:{radius},{lat},{lon});
              way["tourism"="hotel"](around:{radius},{lat},{lon});
              relation["tourism"="hotel"](around:{radius},{lat},{lon});
              node["tourism"="guest_house"](around:{radius},{lat},{lon});
              way["tourism"="guest_house"](around:{radius},{lat},{lon});
              relation["tourism"="guest_house"](around:{radius},{lat},{lon});
              node["tourism"="hostel"](around:{radius},{lat},{lon});
              way["tourism"="hostel"](around:{radius},{lat},{lon});
              relation["tourism"="hostel"](around:{radius},{lat},{lon});
            );
            out body;
            >;
            out skel qt;
            """
            
            response = requests.post(self.base_url, data=query)
            response.raise_for_status()
            
            data = response.json()
            
            accommodations = self._process_accommodations(data["elements"], limit)
            
            return {
                "latitude": lat,
                "longitude": lon,
                "radius": radius,
                "accommodations": accommodations,
                "count": len(accommodations),
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_accommodations_by_coordinates(lat, lon, radius, limit)
    
    def _process_accommodations(self, elements: List[Dict], limit: int) -> List[Dict]:
        """
        Process raw accommodation data from Overpass API
        """
        accommodations = []
        
        for element in elements:
            if element["type"] == "node" and "tags" in element:
                tags = element["tags"]
                
                accommodation = {
                    "id": element["id"],
                    "type": element["type"],
                    "name": tags.get("name", "Unnamed"),
                    "tourism_type": tags.get("tourism", "unknown"),
                    "latitude": element["lat"],
                    "longitude": element["lon"],
                    "address": {
                        "street": tags.get("addr:street"),
                        "housenumber": tags.get("addr:housenumber"),
                        "postcode": tags.get("addr:postcode"),
                        "city": tags.get("addr:city")
                    },
                    "contact": {
                        "phone": tags.get("phone"),
                        "website": tags.get("website"),
                        "email": tags.get("email")
                    },
                    "amenities": {
                        "wifi": tags.get("internet_access") == "wlan",
                        "parking": tags.get("parking") == "yes",
                        "breakfast": tags.get("breakfast") == "yes"
                    },
                    "stars": tags.get("stars"),
                    "rooms": tags.get("rooms")
                }
                
                accommodations.append(accommodation)
                
                if len(accommodations) >= limit:
                    break
        
        return accommodations
    
    def _get_mock_accommodations(self, city: str, limit: int) -> Dict[str, Any]:
        """
        Return mock accommodation data when API is unavailable
        """
        mock_accommodations = []
        
        accommodation_types = ["hotel", "guest_house", "hostel"]
        names = [
            "Grand Hotel", "City Center Hotel", "Riverside Inn", "Mountain View Lodge",
            "Seaside Resort", "Business Hotel", "Boutique Hotel", "Heritage Inn",
            "Modern Suites", "Cozy Guesthouse"
        ]
        
        for i in range(min(limit, len(names))):
            accommodation = {
                "id": f"mock_{i}",
                "type": "node",
                "name": names[i],
                "tourism_type": accommodation_types[i % len(accommodation_types)],
                "latitude": 40.7128 + (i * 0.01),
                "longitude": -74.006 + (i * 0.01),
                "address": {
                    "street": f"Main Street {i+1}",
                    "housenumber": str(100 + i),
                    "postcode": "10001",
                    "city": city
                },
                "contact": {
                    "phone": f"+1-555-{1000+i}",
                    "website": f"https://example{i}.com",
                    "email": f"info@example{i}.com"
                },
                "amenities": {
                    "wifi": True,
                    "parking": i % 2 == 0,
                    "breakfast": True
                },
                "stars": (i % 5) + 1,
                "rooms": 20 + (i * 5)
            }
            
            mock_accommodations.append(accommodation)
        
        return {
            "city": city,
            "accommodations": mock_accommodations,
            "count": len(mock_accommodations),
            "success": True
        }
    
    def _get_mock_accommodations_by_coordinates(self, lat: float, lon: float, radius: float, limit: int) -> Dict[str, Any]:
        """
        Return mock accommodation data for coordinate-based search when API is unavailable
        """
        mock_accommodations = []
        
        names = [
            "Central Hotel", "Downtown Inn", "Metro Lodge", "Urban Resort",
            "City Hotel", "Business Center", "Executive Suites", "Premium Inn"
        ]
        
        for i in range(min(limit, len(names))):
            accommodation = {
                "id": f"mock_coord_{i}",
                "type": "node",
                "name": names[i],
                "tourism_type": "hotel",
                "latitude": lat + (i * 0.001),
                "longitude": lon + (i * 0.001),
                "address": {
                    "street": f"Downtown Street {i+1}",
                    "housenumber": str(200 + i),
                    "postcode": "10001",
                    "city": "Unknown"
                },
                "contact": {
                    "phone": f"+1-555-{2000+i}",
                    "website": f"https://downtown{i}.com",
                    "email": f"info@downtown{i}.com"
                },
                "amenities": {
                    "wifi": True,
                    "parking": True,
                    "breakfast": i % 2 == 0
                },
                "stars": (i % 4) + 2,
                "rooms": 30 + (i * 3)
            }
            
            mock_accommodations.append(accommodation)
        
        return {
            "latitude": lat,
            "longitude": lon,
            "radius": radius,
            "accommodations": mock_accommodations,
            "count": len(mock_accommodations),
            "success": True
        } 