from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime

class RateInfo(BaseModel):
    cbn_official: float = Field(..., description="Official Central Bank of Nigeria rate", example=1580.50)
    parallel_market: float = Field(..., description="Black market / Street rate", example=1615.00)

class ExchangeRateResponse(BaseModel):
    timestamp: datetime = Field(..., description="Last updated time (UTC)")
    base_currency: str = Field(..., description="Base currency (always NGN)", example="NGN")
    rates: Dict[str, RateInfo] = Field(..., description="Mapping of international currencies to NGN rates")

class FuelPriceResponse(BaseModel):
    timestamp: datetime = Field(..., description="Last updated time (UTC)")
    currency: str = Field(..., description="Currency (always NGN)", example="NGN")
    prices_per_litre: Dict[str, float] = Field(..., description="Fuel type prices (PMS, Diesel, etc.)")
    note: str = Field(..., description="Contextual note on regional variations")

class CommodityPriceResponse(BaseModel):
    timestamp: datetime = Field(..., description="Last updated time (UTC)")
    currency: str = Field(..., description="Currency (always NGN)", example="NGN")
    commodities: Dict[str, float] = Field(..., description="Key Nigerian commodity prices (Rice, Cement, etc.)")

class ErrorResponse(BaseModel):
    detail: str = Field(..., description="Detailed error message")
    code: str = Field(..., description="Internal application-specific error code")
