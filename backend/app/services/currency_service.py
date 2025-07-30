import requests
from typing import Dict, Any, Optional
from app.config import settings


class CurrencyService:
    def __init__(self):
        self.base_url = settings.exchangerate_api_url
        
    def convert_currency(self, from_currency: str, to_currency: str, amount: float = 1.0) -> Dict[str, Any]:
        """
        Convert currency using ExchangeRate.host API
        """
        try:
            url = f"{self.base_url}/convert"
            params = {
                "from": from_currency.upper(),
                "to": to_currency.upper(),
                "amount": amount
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "from_currency": from_currency.upper(),
                "to_currency": to_currency.upper(),
                "amount": amount,
                "converted_amount": data["result"],
                "rate": data["info"]["rate"],
                "timestamp": data["info"]["timestamp"]
            }
            
        except requests.RequestException as e:
            return self._get_mock_conversion(from_currency, to_currency, amount)
    
    def get_exchange_rates(self, base_currency: str = "USD") -> Dict[str, Any]:
        """
        Get all exchange rates for a base currency
        """
        try:
            url = f"{self.base_url}/latest"
            params = {
                "base": base_currency.upper()
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "base_currency": base_currency.upper(),
                "date": data["date"],
                "rates": data["rates"],
                "timestamp": data.get("timestamp")
            }
            
        except requests.RequestException as e:
            return self._get_mock_rates(base_currency)
    
    def get_historical_rates(self, date: str, base_currency: str = "USD") -> Dict[str, Any]:
        """
        Get historical exchange rates for a specific date
        """
        try:
            url = f"{self.base_url}/{date}"
            params = {
                "base": base_currency.upper()
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "base_currency": base_currency.upper(),
                "date": data["date"],
                "rates": data["rates"]
            }
            
        except requests.RequestException as e:
            return self._get_mock_historical_rates(date, base_currency)
    
    def get_currency_list(self) -> Dict[str, Any]:
        """
        Get list of supported currencies
        """
        try:
            url = f"{self.base_url}/symbols"
            
            response = requests.get(url)
            response.raise_for_status()
            
            data = response.json()
            
            return {
                "currencies": data["symbols"]
            }
            
        except requests.RequestException as e:
            return self._get_mock_currency_list()
    
    def _get_mock_conversion(self, from_currency: str, to_currency: str, amount: float) -> Dict[str, Any]:
        """
        Return mock conversion data when API is unavailable
        """
        # Mock exchange rates for common currencies
        mock_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
            "JPY": 110.0,
            "CAD": 1.25,
            "AUD": 1.35,
            "CHF": 0.92,
            "CNY": 6.45,
            "INR": 74.5,
            "BRL": 5.2
        }
        
        from_rate = mock_rates.get(from_currency.upper(), 1.0)
        to_rate = mock_rates.get(to_currency.upper(), 1.0)
        rate = to_rate / from_rate
        
        return {
            "from_currency": from_currency.upper(),
            "to_currency": to_currency.upper(),
            "amount": amount,
            "converted_amount": amount * rate,
            "rate": rate,
            "timestamp": 1640995200
        }
    
    def _get_mock_rates(self, base_currency: str) -> Dict[str, Any]:
        """
        Return mock exchange rates when API is unavailable
        """
        mock_rates = {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
            "JPY": 110.0,
            "CAD": 1.25,
            "AUD": 1.35,
            "CHF": 0.92,
            "CNY": 6.45,
            "INR": 74.5,
            "BRL": 5.2
        }
        
        base_rate = mock_rates.get(base_currency.upper(), 1.0)
        rates = {}
        
        for currency, rate in mock_rates.items():
            if currency != base_currency.upper():
                rates[currency] = rate / base_rate
        
        return {
            "base_currency": base_currency.upper(),
            "date": "2024-01-01",
            "rates": rates,
            "timestamp": 1640995200
        }
    
    def _get_mock_historical_rates(self, date: str, base_currency: str) -> Dict[str, Any]:
        """
        Return mock historical rates when API is unavailable
        """
        return self._get_mock_rates(base_currency)
    
    def _get_mock_currency_list(self) -> Dict[str, Any]:
        """
        Return mock currency list when API is unavailable
        """
        currencies = {
            "USD": {"description": "US Dollar", "code": "USD"},
            "EUR": {"description": "Euro", "code": "EUR"},
            "GBP": {"description": "British Pound", "code": "GBP"},
            "JPY": {"description": "Japanese Yen", "code": "JPY"},
            "CAD": {"description": "Canadian Dollar", "code": "CAD"},
            "AUD": {"description": "Australian Dollar", "code": "AUD"},
            "CHF": {"description": "Swiss Franc", "code": "CHF"},
            "CNY": {"description": "Chinese Yuan", "code": "CNY"},
            "INR": {"description": "Indian Rupee", "code": "INR"},
            "BRL": {"description": "Brazilian Real", "code": "BRL"}
        }
        
        return {
            "currencies": currencies
        } 