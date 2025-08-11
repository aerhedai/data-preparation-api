from fastapi import FastAPI
from app.api.routes import router
from app.utils.logging import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Data Preparation API",
    description="Handles imputation, feature engineering, and leakage detection",
    version="1.0.0"
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Data Preparation API started.")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("🛑 Data Preparation API stopped.")
