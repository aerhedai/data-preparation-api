import pandas as pd
from app.models.leakage_schema import LeakageRequest, LeakageResponse

def check_leakage(data: LeakageRequest) -> LeakageResponse:
    df = pd.DataFrame(data.rows)
    target = data.target_column

    leakage_warnings = []

    if target in df.columns:
        correlations = df.corr(numeric_only=True)[target].abs()
        high_corr_features = correlations[correlations > 0.95].index.tolist()
        high_corr_features.remove(target)
        if high_corr_features:
            leakage_warnings.append(
                f"Possible leakage from features: {', '.join(high_corr_features)}"
            )

    return LeakageResponse(leakage_found=len(leakage_warnings) > 0, details=leakage_warnings)
