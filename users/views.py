from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from users.forms import RegistrationForm, UserUpdateForm


class ProfileView(View):
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=kwargs['pk'])
        return render(request, self.template_name, {"user": user})


class ProfileUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("vpn_service:index")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj != self.request.user:
            raise HttpResponseForbidden("You don't have permission to access this page")
        return obj

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating profile.')
        return super().form_invalid(form)


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
