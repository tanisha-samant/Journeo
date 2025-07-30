from fastapi import APIRouter, HTTPException
from app.services.accommodation_service import AccommodationService

router = APIRouter(prefix="/api/accommodations", tags=["accommodations"])

accommodation_service = AccommodationService()


@router.get("/{city}")
async def find_accommodations(city: str, limit: int = 10):
    """
    Find accommodations in a city
    """
    try:
        accommodations = accommodation_service.find_accommodations(city, limit)
        return accommodations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error finding accommodations: {str(e)}")


@router.get("/coordinates/{lat}/{lon}")
async def find_accommodations_by_coordinates(lat: float, lon: float, radius: float = 5000, limit: int = 10):
    """
    Find accommodations near specific coordinates
    """
    try:
        accommodations = accommodation_service.find_accommodations_by_coordinates(lat, lon, radius, limit)
        return accommodations
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error finding accommodations: {str(e)}") 