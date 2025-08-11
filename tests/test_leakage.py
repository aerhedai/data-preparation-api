from app.services.leakage import check_leakage
from app.models.leakage_schema import LeakageRequest

def test_check_leakage():
    data = LeakageRequest(
        rows=[{"target": 1, "x": 1}, {"target": 2, "x": 2}],
        target_column="target"
    )
    result = check_leakage(data)
    assert isinstance(result.leakage_found, bool)
