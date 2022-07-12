from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
from django.urls import reverse

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

    @property
    def total_invoiced_amount(self):
        """
        Calculates and returns the sum of all invoices amount related to the user
        :return: Sum of all user invoiced amounts
        :rtype: float
        """
        return self.invoice_set.aggregate(Sum("amount"))["amount__sum"] or float(0)

    def get_full_name(self):
        """
        Returns the full name of the user composed by first_name and last_name,
        both separated by a space
        :return: Full name of the user
        :rtype: str
        """
        return " ".join([self.first_name, self.last_name]).strip()

    def get_invoices_admin_url(self):
        link = ""
        if self.pk:
            base_url = reverse("admin:invoices_invoice_changelist")
            get_filter = f"?user__id__exact={self.pk}"
            link = base_url + get_filter
        return link
