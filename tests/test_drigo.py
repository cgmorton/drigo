import drigo

test_geo = [1, 2, 3, 4, 5, 6]

def test_geo_origin():
    assert drigo.geo_origin(test_geo) == (test_geo[0], test_geo[3])
