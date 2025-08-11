from app.models.imputation_schema import ImputationRequest, ImputationResponse
import pandas as pd

def suggest_imputation(data: ImputationRequest) -> ImputationResponse:
    df = pd.DataFrame(data.rows)
    suggestions = {col: ("median" if df[col].dtype != object else "mode") for col in df.columns}
    return ImputationResponse(imputation_methods=suggestions)
