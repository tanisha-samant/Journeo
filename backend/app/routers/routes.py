from fastapi import APIRouter, HTTPException
from app.schemas.trip import RouteRequest
from app.services.route_service import RouteService

router = APIRouter(prefix="/api/routes", tags=["routes"])

route_service = RouteService()


@router.get("/")
async def get_route(start: str, end: str, mode: str = "driving"):
    """
    Get route between two points
    """
    try:
        route = route_service.get_route(start, end, mode)
        return route
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching route: {str(e)}")


@router.get("/multimodal")
async def get_multimodal_route(start: str, end: str):
    """
    Get multimodal route suggestions
    """
    try:
        routes = route_service.get_multimodal_route(start, end)
        return routes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching multimodal routes: {str(e)}")


@router.post("/")
async def get_route_post(request: RouteRequest):
    """
    Get route using POST request
    """
    try:
        route = route_service.get_route(request.start, request.end, request.mode)
        return route
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching route: {str(e)}") 