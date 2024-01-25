from django.urls import path

from users.views import register_view, ProfileUpdateView, ProfileView

urlpatterns = [
    path("", register_view, name="register"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path(
        "profile/<int:pk>/edit/",
        ProfileUpdateView.as_view(),
        name="profile_edit"
    ),
]

app_name = "users"
