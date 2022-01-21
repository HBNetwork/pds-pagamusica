from decimal import Decimal, ROUND_HALF_UP


class Money(Decimal):
    def __new__(cls, value, precision=2):
        number = super().__new__(cls, value)
        # algo acontece e arredonda se precisar.
        if not number._is_precise(precision):
            number = number._round(precision)
        return number

    def __repr__(self):
        return "{0}({1!r})".format(self.__class__.__name__, super().__str__())
    
    def __str__(self):
        return "{:n}".format(self)

    def _is_precise(self, precision):
        return abs(self.as_tuple().exponent) == precision

    def _round(self, precision):
        number = self.quantize(
            Decimal(10) ** (-precision), rounding=ROUND_HALF_UP
        )
        return Money(number, precision=precision)
