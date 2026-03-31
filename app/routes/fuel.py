from fastapi import APIRouter, HTTPException
from app.models.schemas import FuelPriceResponse, ErrorResponse
from app.services.data_service import data_service

router = APIRouter(prefix="/rates", tags=["Economic Indicators"])

@router.get(
    "/fuel",
    response_model=FuelPriceResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get Fuel Pump prices",
    description="Returns national average pump prices per litre for PMS, Diesel and Kerosene."
)
async def get_fuel_prices():
    """
    Fetch national average fuel prices from market indicators.
    - **PMS**: National average
    - **Diesel**: National average
    - **Kerosene**: National average
    """
    try:
        return data_service.get_latest_fuel_prices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
