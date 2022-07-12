from rest_framework.decorators import api_view, action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from rest_framework.viewsets import GenericViewSet

from api.invoices.serializers import InvoiceSerializer
from api.users.serializers import UserSerializer
from users.models import User


class UserViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=["get"])
    def unpaid_invoices(self, request, *args, **kwargs):
        instance = self.get_object()
        invoices = instance.invoice_set.filter(paid=False)
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def get_user_invoices(request, user_id):
    return None
