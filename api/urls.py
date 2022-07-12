from django.urls import include, path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("invoices/", include("api.invoices.urls")),
    path("", include("api.users.urls"))
]
