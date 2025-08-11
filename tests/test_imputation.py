from app.services.imputation import suggest_imputation
from app.models.imputation_schema import ImputationRequest

def test_suggest_imputation():
    data = ImputationRequest(rows=[{"a": 1, "b": None}, {"a": 2, "b": "x"}])
    result = suggest_imputation(data)
    assert "a" in result.imputation_methods
