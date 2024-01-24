from django.urls import path

from vpn_service.views import index, statistics

urlpatterns = [
    path("", index, name="index"),
    path('statistics/', statistics, name='statistics'),
]

app_name = "vpn_service"
