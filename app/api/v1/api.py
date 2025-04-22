"""API V1 for vibradev-py

This module sets up the main API router and includes all sub-routers for the application.
Includes endpoints for authentication and chatbot functionality.
"""

from fastapi import APIRouter, FastAPI

# from app.api.v1.auth import router as auth_router
# from app.api.v1.chatbot import router as chatbot_router
import logging
import os

api_router = APIRouter()
logger = logging.getLogger(__name__)
# Include all sub-routers here

# api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
# api_router.include_router(chatbot_router, prefix="/chatbot", tags=["chatbot"])



@api_router.get("/health")
async def health_check():
    """
    Health check endpoint to verify if the API is running.
    """
    # get os env value 
    appVersion = os.getenv("APP_VERSION", "1.0.0")
    logger.info("Health check endpoint called.")
    return {"status": "ok", "version": appVersion}

@api_router.get("/live")
async def liveness_check():
    """
    Liveness check endpoint to verify if the API is alive.
    """
    logger.info("Liveness check endpoint called.")
    return {"status": "alive"}

@api_router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint to verify if the API is ready to serve requests.
    """
    logger.info("Readiness check endpoint called.")
    return {"status": "ready"}

app = FastAPI(title = "Gym Chatbot Agent")
app.include_router(api_router, prefix="/api/v1", tags=["v1"])