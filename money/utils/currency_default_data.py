def get_currency_data():
    """
    This is a mock of a method that could consult a currencies API with updated conversion rates.
    :return: List of with currency objects in dictionary form
    :rtype: List[Dict]
    """
    currencies = [
        {
            "name": "United States Dollar",
            "code": "USD",
            "conversion_rate": "1.0",
            "active": "True",
        },
        {
            "name": "Euro",
            "code": "EUR",
            "conversion_rate": "1.02",
            "active": "True",
        },
    ]
    return currencies
