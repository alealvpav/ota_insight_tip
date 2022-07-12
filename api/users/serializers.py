from rest_framework.serializers import ModelSerializer

from invoices.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
