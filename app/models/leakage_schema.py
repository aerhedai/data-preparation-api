from pydantic import BaseModel
from typing import List, Dict, Any

class LeakageRequest(BaseModel):
    rows: List[Dict[str, Any]]
    target_column: str

class LeakageResponse(BaseModel):
    leakage_found: bool
    details: List[str]
