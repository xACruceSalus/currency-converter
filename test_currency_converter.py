from currency_converter import convert


rates = [("USD", "EUR", 0.74)]
value = 1
a_from = 'USD'
a_to = 'EUR'

def test_convert():
    assert convert(rates, value, 'USD', 'USD') == 1

def test_simple_conversion():
    assert convert(rates, value, a_from, a_to) == .74

def test_different_values():
    assert convert(rates, 10, a_from, a_to) == 7.4
    assert convert(rates, 50, a_from, a_to) == 37
    assert int(convert(rates, 1.5, a_from, a_to)) == 1

def test_reverse_lookup():
    assert convert([("EUR", "USD", 0.74)], value, a_from, a_to) == 1.35
