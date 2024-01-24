from django.urls import path

from vpn_service.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "vpn_service"
