from currency_converter import convert


def test_convert():
    rates = [("USD", "EUR", 0.74)]
    value = 100
    a_from = 'USD'
    a_to = 'USD'
    assert convert(rates, value, a_from, a_to) == 100
