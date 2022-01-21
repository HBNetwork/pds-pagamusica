from money import Money


def test_money():
    
    assert str(Money("0")) == "0.00"
    assert str(Money(".00")) == "0.00"
    
    assert Money("1.2345") == Money("1.23")
    assert Money("1.235") == Money("1.24")
    
    assert str(Money("1.1234", precision=3)) == "1.123"
    
    assert repr(Money("0")) == "Money('0.00')"
    
    import locale
    
    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, "pt_BR")
    assert str(Money("1.42")) == "1,42"
    locale.setlocale(locale.LC_ALL, loc)
    