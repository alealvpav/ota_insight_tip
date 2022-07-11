from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField

from money.models import Currency


class User(AbstractUser):
    # AbstractUser already has email, username, first_name and last_name.
    email = models.EmailField(blank=False)
    company_name = models.CharField(max_length=200, blank=True, default="")
    country = CountryField()
    # I assume that accepted currencies is a field that can vary in time, and
    # it's easier to maintain a table in a database from django admin than a
    # list of choices, this way it does not depend on developers.
    invoice_currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        default=1,  # Default: USD
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Returns the full name of the user composed by first_name and last_name,
        both separated by a space
        :return: Full name of the user
        :rtype: str
        """
        return " ".join([self.first_name, self.last_name]).strip()
