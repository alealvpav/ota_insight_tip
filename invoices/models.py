from django.db import models
from shortuuid.django_fields import ShortUUIDField

from invoices.utils import LogicalDeleteAbstractModel
from users.models import User


class Invoice(LogicalDeleteAbstractModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    number = ShortUUIDField(
        length=5,
        max_length=9,
        prefix="OTA-",
        alphabet="0123456789",
        unique=True,
        # I understood only numbers were valid, but if letters are also allowed they
        # just need to be added to the alphabet string
    )
    amount = models.FloatField(blank=False)
    paid = models.BooleanField(default=False)
    # I assumed it could only be paid or not, but status choices was another option.
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number

    def get_invoiced_currency(self):
        """
        Invoice is related to the user invoiced
        :return: Invoiced user's currency
        :rtype: Currency
        """
        return self.user.invoice_currency


