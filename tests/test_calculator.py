from demo_ci.calculator import average, greet


def test_average() -> None:
    assert average([1.0, 2.0, 3.0]) == 2.0


def test_average_empty() -> None:
    assert average([]) == 0


def test_greet() -> None:
    assert greet("An") == "Xin chào, An"
