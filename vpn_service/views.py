from django.shortcuts import render
from .models import SiteStatistics


def index(request):
    return render(request, 'vpn_service/index.html')


def statistics(request):
    statistics_data = SiteStatistics.objects.filter(user=request.user)
    return render(request, 'vpn_service/statistics.html', {'statistics_data': statistics_data})

