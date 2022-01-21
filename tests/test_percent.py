from percent import Percent
from decimal import Decimal
import pytest


def test_percent():
    assert Percent(0) == 0
    assert Percent(100) == 1
    assert Percent(10) == Decimal("0.1")
    assert Percent("5.5") == Decimal("0.055")
    with pytest.raises(ValueError) as excinfo:
        Percent(-0.1)
        assert "Percent can not be negative." in str(excinfo.value)
    with pytest.raises(ValueError) as excinfo:
        Percent(101)
        assert "Percent can not be greater than 100" in str(excinfo.value)
