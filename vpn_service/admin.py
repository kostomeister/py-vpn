from django.contrib import admin
from .models import Site, SiteStatistics


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("user", 'name', 'url')
    search_fields = ("user", 'name', 'url')


@admin.register(SiteStatistics)
class SiteStatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'site', 'data_size', 'page_transitions_count')
    list_filter = ('user', 'site')
    search_fields = ('user__username', 'site__name')
