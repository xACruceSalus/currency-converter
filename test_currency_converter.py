from currency_converter import convert


rates = [("USD", "EUR", 0.74)]
value = 1
a_from = 'USD'
a_to = 'EUR'

def test_convert():
    a_from = 'USD'
    a_to = 'USD'
    assert convert(rates, value, a_from, a_to) == 1

def test_simple_conversion():
    assert convert(rates, value, a_from, a_to) == .74
