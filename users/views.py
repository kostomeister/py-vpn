from django.contrib.auth import login, get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegistrationForm


class ProfileView(View):
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, {"user": user})


def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()

    return render(request, "registration/register.html", {"form": form})
