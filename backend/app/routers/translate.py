from fastapi import APIRouter, HTTPException
from app.schemas.trip import TranslationRequest
from app.services.translation_service import TranslationService

router = APIRouter(prefix="/api/translate", tags=["translate"])

translation_service = TranslationService()


@router.post("/")
async def translate_text(request: TranslationRequest):
    """
    Translate text to target language
    """
    try:
        result = translation_service.translate_text(
            request.text, 
            request.target_language, 
            request.source_language
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating text: {str(e)}")


@router.post("/itinerary")
async def translate_itinerary(text: str, target_language: str):
    """
    Translate a complete travel itinerary
    """
    try:
        result = translation_service.translate_itinerary(text, target_language)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error translating itinerary: {str(e)}")


@router.get("/languages")
async def get_supported_languages():
    """
    Get list of supported languages
    """
    try:
        languages = translation_service.get_supported_languages()
        return languages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching languages: {str(e)}")


@router.post("/detect")
async def detect_language(text: str):
    """
    Detect the language of the input text
    """
    try:
        result = translation_service.detect_language(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detecting language: {str(e)}") 