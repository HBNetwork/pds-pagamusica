from decimal import Decimal


class Percent(Decimal):
    def __new__(cls, value):
        number = super().__new__(cls, value)
        if number < 0:
            raise ValueError("Percent can not be negative.")
        if number > 100:
            raise ValueError("Percent can not be greater than 100")
        number = number / 100
        return number
