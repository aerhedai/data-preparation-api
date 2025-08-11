from fastapi import APIRouter
from app.services.imputation import suggest_imputation
from app.services.features import create_features
from app.services.leakage import check_leakage

from app.models.imputation_schema import ImputationRequest, ImputationResponse
from app.models.features_schema import FeaturesRequest, FeaturesResponse
from app.models.leakage_schema import LeakageRequest, LeakageResponse

router = APIRouter()

@router.post("/impute", response_model=ImputationResponse)
def impute(data: ImputationRequest):
    return suggest_imputation(data)

@router.post("/features", response_model=FeaturesResponse)
def features(data: FeaturesRequest):
    return create_features(data)

@router.post("/leakage", response_model=LeakageResponse)
def leakage(data: LeakageRequest):
    return check_leakage(data)
