from app.services.features import create_features
from app.models.features_schema import FeaturesRequest

def test_create_features():
    data = FeaturesRequest(rows=[{"a": 1, "b": 2}, {"a": 3, "b": 4}])
    result = create_features(data)
    assert any(col.endswith("_squared") for col in result.new_features)
