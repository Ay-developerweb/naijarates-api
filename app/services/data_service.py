import logging
from datetime import datetime
from typing import Dict, Any
from app.db.database import SessionLocal, RateData

logger = logging.getLogger("naijarates-data-service")

class DataService:
    def _fetch_from_db(self, category: str) -> Dict[str, Any]:
        """ Internal helper to pull data from DB and handle empty states. """
        db = SessionLocal()
        try:
            rate_entry = db.query(RateData).filter(RateData.category == category).first()
            if not rate_entry:
                logger.warning(f"No current data for {category}, returning fallback.")
                return {}
            # SQL Alchemy JSON handles deserialization for us
            return rate_entry.data
        except Exception as e:
            logger.error(f"Error fetching {category} from DB: {e}")
            return {}
        finally:
            db.close()

    def get_latest_exchange_rates(self) -> Dict[str, Any]:
        """ Fetches processed exchange rate data from database. """
        return self._fetch_from_db("exchange")

    def get_latest_fuel_prices(self) -> Dict[str, Any]:
        """ Fetches processed fuel price data from database. """
        return self._fetch_from_db("fuel")

    def get_latest_commodity_prices(self) -> Dict[str, Any]:
        """ Fetches processed commodity price data from database. """
        return self._fetch_from_db("commodities")

data_service = DataService()
