from django.urls import path

from vpn_service.views import (
    index,
    statistics,
    user_urls,
    delete_url,
    update_url,
    proxy_view,
)

urlpatterns = [
    path("", index, name="index"),
    path("statistics/", statistics, name="statistics"),
    path("urls/", user_urls, name="user_urls"),
    path("update_url/<int:url_id>/", update_url, name="update_url"),
    path("delete_url/<int:url_id>/", delete_url, name="delete_url"),
    path(
        "<str:site_name>/<path:routes_on_original_site>/",
        proxy_view,
        name="proxy_view"
    ),
]

app_name = "vpn_service"
