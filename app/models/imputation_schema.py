from pydantic import BaseModel
from typing import List, Dict, Any

class ImputationRequest(BaseModel):
    rows: List[Dict[str, Any]]

class ImputationResponse(BaseModel):
    imputation_methods: Dict[str, str]
