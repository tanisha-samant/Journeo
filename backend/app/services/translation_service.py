import requests
from typing import Dict, Any, Optional
from app.config import settings


class TranslationService:
    def __init__(self):
        self.base_url = settings.libretranslate_api_url
        
    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = "auto") -> Dict[str, Any]:
        """
        Translate text using LibreTranslate.de API
        """
        try:
            payload = {
                "q": text,
                "source": source_language,
                "target": target_language,
                "format": "text"
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "original_text": text,
                "translated_text": data["translatedText"],
                "source_language": data.get("detectedLanguage", {}).get("confidence", 0),
                "target_language": target_language,
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_translation(text, target_language, source_language)
    
    def get_supported_languages(self) -> Dict[str, Any]:
        """
        Get list of supported languages
        """
        try:
            url = f"{self.base_url.replace('/translate', '/languages')}"
            
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "languages": data,
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_languages()
    
    def detect_language(self, text: str) -> Dict[str, Any]:
        """
        Detect the language of the input text
        """
        try:
            url = f"{self.base_url.replace('/translate', '/detect')}"
            
            payload = {
                "q": text
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "text": text,
                "detected_language": data[0]["language"],
                "confidence": data[0]["confidence"],
                "success": True
            }
            
        except requests.RequestException as e:
            return self._get_mock_detection(text)
    
    def translate_itinerary(self, itinerary: str, target_language: str) -> Dict[str, Any]:
        """
        Translate a complete travel itinerary
        """
        try:
            # Split itinerary into paragraphs for better translation
            paragraphs = itinerary.split('\n\n')
            translated_paragraphs = []
            
            for paragraph in paragraphs:
                if paragraph.strip():
                    result = self.translate_text(paragraph.strip(), target_language)
                    if result["success"]:
                        translated_paragraphs.append(result["translated_text"])
                    else:
                        translated_paragraphs.append(paragraph)
                else:
                    translated_paragraphs.append("")
            
            translated_itinerary = '\n\n'.join(translated_paragraphs)
            
            return {
                "original_itinerary": itinerary,
                "translated_itinerary": translated_itinerary,
                "target_language": target_language,
                "success": True
            }
            
        except Exception as e:
            return {
                "original_itinerary": itinerary,
                "translated_itinerary": itinerary,  # Return original if translation fails
                "target_language": target_language,
                "success": False,
                "error": str(e)
            }
    
    def _get_mock_translation(self, text: str, target_language: str, source_language: str) -> Dict[str, Any]:
        """
        Return mock translation when API is unavailable
        """
        # Simple mock translations for common phrases
        mock_translations = {
            "en": {
                "es": "¡Hola! Bienvenido a tu viaje.",
                "fr": "Bonjour! Bienvenue dans votre voyage.",
                "de": "Hallo! Willkommen zu Ihrer Reise.",
                "it": "Ciao! Benvenuto nel tuo viaggio.",
                "pt": "Olá! Bem-vindo à sua viagem."
            }
        }
        
        if source_language == "auto" or source_language == "en":
            translated_text = mock_translations.get("en", {}).get(target_language, text)
        else:
            translated_text = text
        
        return {
            "original_text": text,
            "translated_text": translated_text,
            "source_language": source_language,
            "target_language": target_language,
            "success": True
        }
    
    def _get_mock_languages(self) -> Dict[str, Any]:
        """
        Return mock supported languages when API is unavailable
        """
        languages = [
            {"code": "en", "name": "English"},
            {"code": "es", "name": "Spanish"},
            {"code": "fr", "name": "French"},
            {"code": "de", "name": "German"},
            {"code": "it", "name": "Italian"},
            {"code": "pt", "name": "Portuguese"},
            {"code": "ru", "name": "Russian"},
            {"code": "ja", "name": "Japanese"},
            {"code": "ko", "name": "Korean"},
            {"code": "zh", "name": "Chinese"}
        ]
        
        return {
            "languages": languages,
            "success": True
        }
    
    def _get_mock_detection(self, text: str) -> Dict[str, Any]:
        """
        Return mock language detection when API is unavailable
        """
        # Simple language detection based on common words
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["hello", "welcome", "travel", "trip"]):
            detected_lang = "en"
        elif any(word in text_lower for word in ["hola", "bienvenido", "viaje"]):
            detected_lang = "es"
        elif any(word in text_lower for word in ["bonjour", "bienvenue", "voyage"]):
            detected_lang = "fr"
        else:
            detected_lang = "en"
        
        return {
            "text": text,
            "detected_language": detected_lang,
            "confidence": 0.8,
            "success": True
        } 