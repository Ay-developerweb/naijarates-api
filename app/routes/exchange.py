from fastapi import APIRouter, HTTPException
from app.models.schemas import ExchangeRateResponse, ErrorResponse
from app.services.data_service import data_service

router = APIRouter(prefix="/rates", tags=["Economic Indicators"])

@router.get(
    "/exchange",
    response_model=ExchangeRateResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get Exchange Rates",
    description="Returns latest exchange rates for NGN against major currencies (CBN vs Market Parallel)."
)
async def get_exchange_rates():
    """
    Fetch exchange rates from consolidated data source.
    - **USD**: CBN vs Parallel
    - **GBP**: CBN vs Parallel
    - **EUR**: CBN vs Parallel
    """
    try:
        return data_service.get_latest_exchange_rates()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
