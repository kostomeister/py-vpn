import sys

from vpn_service.models import SiteStatistics


def update_site_statistics(user, site, data):
    size_of_data = sys.getsizeof(data)

    site_statistics, created = SiteStatistics.objects.get_or_create(
        site=site, user=user
    )
    site_statistics.data_size += size_of_data
    site_statistics.page_transitions_count += 1

    site_statistics.save()
