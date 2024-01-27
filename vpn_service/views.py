from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import URLForm
from .models import Site, SiteStatistics
from .parse import ContentProcessor, RequestHandler
from .utils import update_site_statistics


def index(request):
    return render(request, "vpn_service/index.html")


def statistics(request):
    statistics_data = SiteStatistics.objects.filter(user=request.user)
    return render(
        request,
        "vpn_service/statistics.html",
        {"statistics_data": statistics_data}
    )


@login_required
def user_urls(request):
    user = request.user
    user_sites = Site.objects.filter(user=user)

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user_id = request.user.id
            site.save()
            return redirect("vpn_service:user_urls")
    else:
        form = URLForm()

    return render(
        request,
        "vpn_service/user_urls.html",
        {"user_sites": user_sites, "form": form}
    )


@login_required
def update_url(request, url_id):
    user_url = get_object_or_404(Site, id=url_id)
    if request.method == "POST":
        form = URLForm(request.POST, instance=user_url)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            return redirect("vpn_service:user_urls")
    else:
        form = URLForm(instance=user_url)
    return render(
        request,
        "vpn_service/update_url.html",
        {"form": form, "user_url": user_url}
    )


@login_required
def delete_url(request, url_id):
    user_url = get_object_or_404(Site, id=url_id, user=request.user)

    if request.method == "GET":
        user_url.delete()

    return redirect("vpn_service:user_urls")


@login_required
@csrf_exempt
def proxy_view(request, site_name, routes_on_original_site):
    target_url = f"https://{routes_on_original_site}"

    site = get_object_or_404(Site, name=site_name)
    base_url = site.url

    with RequestHandler() as request_handler:
        if request.method == "GET":
            response = request_handler.send_get(target_url)

        if request.method == "POST":
            response = request_handler.send_post(
                request.POST.copy(),
                target_url,
                request.COOKIES.get("csrftoken")
            )

    soup = ContentProcessor.get_soup(response.content)

    update_site_statistics(request.user, site, response)

    ContentProcessor.process_static_content(soup, target_url)
    ContentProcessor.process_links(soup, site_name, base_url)

    return HttpResponse(
        str(soup),
        status=response.status_code,
    )
