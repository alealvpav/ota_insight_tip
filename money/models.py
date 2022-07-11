from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)  # ISO 4217
    # Conversion rate is compared to USD:
    # Amount of USD that 1 <Currency> is valued.
    conversion_rate = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "currencies"

    def get_value_in_dollars(self, value):
        """
        Converts the input value to USD.
        :param value: Value (money amount) to be converted
        :type value: Number (Integer/Float)
        :return: value converted to USD
        :rtype: Float
        """
        return value * self.conversion_rate

    def convert_to_currency(self, value, new_currency):
        """
        Converts the input value to the specified new_currency
        :param value: Value (money amount) to be converted
        :type value: Number (Integer/Float)
        :param new_currency: The currency (Currency Object) we want our value to be converted to
        :type new_currency: Currency
        :return: value converted to new_currency
        :rtype: Float
        """
        usd_value = self.get_value_in_dollars(value)
        return usd_value / new_currency.conversion_rate
