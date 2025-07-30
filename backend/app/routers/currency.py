from fastapi import APIRouter, HTTPException
from app.schemas.trip import CurrencyRequest
from app.services.currency_service import CurrencyService

router = APIRouter(prefix="/api/currency", tags=["currency"])

currency_service = CurrencyService()


@router.get("/convert")
async def convert_currency(from_currency: str, to_currency: str, amount: float = 1.0):
    """
    Convert currency
    """
    try:
        result = currency_service.convert_currency(from_currency, to_currency, amount)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error converting currency: {str(e)}")


@router.get("/rates")
async def get_exchange_rates(base_currency: str = "USD"):
    """
    Get all exchange rates for a base currency
    """
    try:
        rates = currency_service.get_exchange_rates(base_currency)
        return rates
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching exchange rates: {str(e)}")


@router.get("/historical/{date}")
async def get_historical_rates(date: str, base_currency: str = "USD"):
    """
    Get historical exchange rates for a specific date
    """
    try:
        rates = currency_service.get_historical_rates(date, base_currency)
        return rates
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching historical rates: {str(e)}")


@router.get("/currencies")
async def get_currencies():
    """
    Get list of supported currencies
    """
    try:
        currencies = currency_service.get_currency_list()
        return currencies
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching currencies: {str(e)}")


@router.post("/convert")
async def convert_currency_post(request: CurrencyRequest):
    """
    Convert currency using POST request
    """
    try:
        result = currency_service.convert_currency(
            request.from_currency, 
            request.to_currency, 
            request.amount
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error converting currency: {str(e)}") 