from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
