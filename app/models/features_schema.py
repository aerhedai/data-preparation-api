from pydantic import BaseModel
from typing import List, Dict, Any

class FeaturesRequest(BaseModel):
    rows: List[Dict[str, Any]]

class FeaturesResponse(BaseModel):
    rows: List[Dict[str, Any]]
    new_features: List[str]
