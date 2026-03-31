from fastapi import APIRouter, HTTPException
from app.models.schemas import CommodityPriceResponse, ErrorResponse
from app.services.data_service import data_service

router = APIRouter(prefix="/rates", tags=["Economic Indicators"])

@router.get(
    "/commodities",
    response_model=CommodityPriceResponse,
    responses={500: {"model": ErrorResponse}},
    summary="Get Commodity Prices",
    description="Returns current market prices for key Nigerian commodities (Rice, Cement, Cooking Gas)."
)
async def get_commodity_prices():
    """
    Fetch market prices for 50kg bags of Rice/Cement and Cooking Gas/kg.
    - **Rice**: 50kg bag
    - **Cement**: 50kg bag
    - **Cooking Gas**: per kg
    """
    try:
        return data_service.get_latest_commodity_prices()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
