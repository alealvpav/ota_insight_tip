from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from rest_framework.viewsets import GenericViewSet

from api.invoices.serializers import InvoiceSerializer
from invoices.models import Invoice


class InvoiceViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
