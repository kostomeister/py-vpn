from django.contrib.auth import get_user_model
from django.test import TestCase
from vpn_service.models import Site, SiteStatistics


class SiteModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.site = Site.objects.create(user=self.user, name='Test Site', url='http://example.com')

    def test_site_str_method(self):
        self.assertEqual(str(self.site), 'Test Site')


class SiteStatisticsModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.site = Site.objects.create(user=self.user, name='Test Site', url='http://example.com')
        self.site_statistics = SiteStatistics.objects.create(user=self.user, site=self.site, data_size=100, page_transitions_count=5)

    def test_site_statistics_str_method(self):
        self.assertEqual(str(self.site_statistics), 'testuser - Test Site')
