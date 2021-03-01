from mlproject.distance import haversine

def test_distance():
    assert type(haversine(2, 0, 0, 0)) == float
