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
    assert convert([("EUR", "USD", 0.74)], value, a_from, a_to) == 1.351

def test_multiple_dif_rates():
    new_rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949),
                 ("USD", "MXN", 14.64)]

    assert convert(new_rates, value, 'EUR', 'JPY') == 145.949
    assert convert(new_rates, value, "JPY", "EUR") == .007
    assert convert(new_rates, value, "JPY", "EUR") == .007
    assert convert(new_rates, 500, "MXN", "USD") == 34.153

def BROKEN_test_values_into_new_rates():
    new_rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

    USD_to_EUR = convert(new_rates, value, "USD", "EUR")
    EUR_to_JPY = convert(new_rates, USD_to_EUR, 'EUR', 'JPY')
    JPY_to_USD = convert(new_rates, EUR_to_JPY, 'JPY', 'USD')

    assert JPY_to_USD == 1
