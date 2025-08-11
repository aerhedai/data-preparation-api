import pandas as pd
from app.models.features_schema import FeaturesRequest, FeaturesResponse

def create_features(data: FeaturesRequest) -> FeaturesResponse:
    df = pd.DataFrame(data.rows)

    # Example: creating simple interaction terms
    for col in df.select_dtypes(include="number").columns:
        df[f"{col}_squared"] = df[col] ** 2

    return FeaturesResponse(
        rows=df.to_dict(orient="records"),
        new_features=[col for col in df.columns if col.endswith("_squared")]
    )
