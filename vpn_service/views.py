from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import URLForm
from .models import Site, SiteStatistics


def index(request):
    return render(request, 'vpn_service/index.html')


def statistics(request):
    statistics_data = SiteStatistics.objects.filter(user=request.user)
    return render(request, 'vpn_service/statistics.html', {'statistics_data': statistics_data})


@login_required
def user_urls(request):
    user = request.user
    user_sites = Site.objects.filter(user=user)

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vpn_service:user_urls')
    else:
        form = URLForm()

    return render(request, 'vpn_service/user_urls.html', {'user_sites': user_sites, 'form': form})


@login_required
def update_url(request, url_id):
    user_url = get_object_or_404(Site, id=url_id)
    if request.method == 'POST':
        form = URLForm(request.POST, instance=user_url)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            return redirect('vpn_service:user_urls')
    else:
        form = URLForm(instance=user_url)
    return render(request, 'vpn_service/update_url.html', {'form': form, 'user_url': user_url})


@login_required
def delete_url(request, url_id):
    user_url = get_object_or_404(Site, id=url_id, user=request.user)

    if request.method == 'GET':
        user_url.delete()

    return redirect('vpn_service:user_urls')
