import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import exchange, fuel, commodities
from app.db.database import init_db
from app.scheduler.jobs import start_scheduler
from app.core.config import settings
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("naijarates-api")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    logger.info("Initializing system components...")
    init_db()
    start_scheduler()
    logger.info("Application successfully initialized.")
    yield
    # Shutdown tasks
    logger.info("Shutting down application...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware for web apps / bots
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception caught: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred. Please contact support.", "code": "INTERNAL_SERVER_ERROR"}
    )

# Include routes
app.include_router(exchange.router, prefix=settings.API_V1_STR)
app.include_router(fuel.router, prefix=settings.API_V1_STR)
app.include_router(commodities.router, prefix=settings.API_V1_STR)

@app.get("/", tags=["Health"])
def health_check():
    """ Returns the system status. """
    return {"status": "operational", "version": settings.VERSION}
