import logging
from apscheduler.schedulers.background import BackgroundScheduler
from app.core.config import settings
from app.services.scraper import scraper_engine

logger = logging.getLogger("naijarates-scheduler")

def update_exchange_rates():
    """ Run exchange rates scraper. """
    scraper_engine.scrape_exchange_rates()

def update_fuel_prices():
    """ Run fuel prices scraper. """
    scraper_engine.scrape_fuel_prices()

def update_commodity_prices():
    """ Run commodity prices scraper. """
    scraper_engine.scrape_commodity_prices()

def start_scheduler():
    """ Initialize and start APScheduler with predefined intervals. """
    scheduler = BackgroundScheduler()
    
    # Configure jobs from settings
    scheduler.add_job(update_exchange_rates, 'interval', hours=settings.EXCHANGE_REFRESH_HOURS)
    scheduler.add_job(update_fuel_prices, 'interval', hours=settings.FUEL_REFRESH_HOURS)
    scheduler.add_job(update_commodity_prices, 'interval', hours=settings.COMMODITY_REFRESH_HOURS)
    
    # Run immediate data fetch on startup to populate empty DB
    logger.info("Initializing first data sync at startup...")
    update_exchange_rates()
    update_fuel_prices()
    update_commodity_prices()
    
    scheduler.start()
    logger.info("APScheduler initialized and running background sync jobs.")
