from django.shortcuts import render


def index(request):
    return render(request, 'vpn_service/index.html')
