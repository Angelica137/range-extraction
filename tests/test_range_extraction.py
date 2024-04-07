from src.range_extraction import range_extraction


def test_range_extaction_returns_1():
    assert range_extraction([1]) == "1"
