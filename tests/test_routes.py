from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "operational", "version": settings.VERSION}

def test_get_exchange_rates():
    response = client.get(f"{settings.API_V1_STR}/rates/exchange")
    assert response.status_code == 200
    data = response.json()
    assert "rates" in data
    assert "USD" in data["rates"]

def test_get_fuel_prices():
    response = client.get(f"{settings.API_V1_STR}/rates/fuel")
    assert response.status_code == 200
    data = response.json()
    assert "prices_per_litre" in data
    assert "PMS" in data["prices_per_litre"]

def test_get_commodity_prices():
    response = client.get(f"{settings.API_V1_STR}/rates/commodities")
    assert response.status_code == 200
    data = response.json()
    assert "commodities" in data
    assert "rice_50kg_bag" in data["commodities"]
