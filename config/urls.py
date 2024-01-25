from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", include("users.urls", namespace="users")),
    path("", include("vpn_service.urls", namespace="vpn_service")),
]
