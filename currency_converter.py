def convert(rates, value, a_from, a_to):
    """This function is designed to take in the below arguments and return
    the value in the specified currency.

    rates = a list of tupleswith each tuple containing a currency code
            you can convert from, a currency code you can convert to,
            and a rate
    value = the amount of money you'd like to exchange for
    from = the currency code in the form of a string
    to = the currency code you'd like the value in. also a string"""

    if a_from == a_to:
        return value

    for list_from, list_to, list_rate in rates:
        if list_from == a_from:
            return round(value * list_rate, 2)

        elif list_from == a_to:
            return round(value / list_rate, 2)




if __name__ == '__main__':
    rates = [("USD", "EUR", 0.74)]
    value = 1
    a_from = 'EUR'
    a_to = 'USD'

    print(convert(rates, value, a_from, a_to))
