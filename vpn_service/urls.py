from django.urls import path

from vpn_service.views import index, statistics, user_urls

urlpatterns = [
    path("", index, name="index"),
    path('statistics/', statistics, name='statistics'),
    path("urls/", user_urls, name="user_urls"),
]

app_name = "vpn_service"
