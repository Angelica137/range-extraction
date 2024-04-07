from src.range_extraction import range_extraction


def test_range_extaction_returns_1():
    assert range_extraction([1]) == "1"


def test_range_extaction_returns_1_2_4_6():
    assert range_extraction([1, 2, 4, 6]) == "1,2,4,6"


def test_range_extaction_returns_1_2_3_4_6():
    assert range_extraction([1, 2, 3, 4, 6]) == "1-4,6"
