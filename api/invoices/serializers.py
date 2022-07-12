from rest_framework import serializers

from api.users.serializers import UserSerializer
from invoices.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    amount = serializers.FloatField()
    paid = serializers.BooleanField()
    creation_date = serializers.DateTimeField()

    class Meta:
        model = Invoice
        fields = ("id", "number", "user", "amount", "paid", "creation_date")
