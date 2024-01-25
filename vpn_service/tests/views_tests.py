from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from vpn_service.models import Site, SiteStatistics


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")
        self.site = Site.objects.create(
            user=self.user, name="Test Site", url="http://example.com"
        )

    def test_index_view(self):
        response = self.client.get(reverse("vpn_service:index"))
        self.assertEqual(response.status_code, 200)

    def test_statistics_view(self):
        response = self.client.get(reverse("vpn_service:statistics"))
        self.assertEqual(response.status_code, 200)

    def test_user_urls_view(self):
        response = self.client.get(reverse("vpn_service:user_urls"))
        self.assertEqual(response.status_code, 200)

    def test_update_url_view(self):
        response = self.client.get(
            reverse("vpn_service:update_url", args=[self.site.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_url_view(self):
        response = self.client.get(
            reverse("vpn_service:delete_url", args=[self.site.id])
        )
        self.assertEqual(response.status_code, 302)

    def test_proxy_view_get(self):
        response = self.client.get(
            reverse(
                "vpn_service:proxy_view", args=["Test Site", "www.example.com/page"]
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_proxy_view_post(self):
        response = self.client.post(
            reverse("vpn_service:proxy_view", args=["Test Site", "httpbin.org/post"])
        )
        self.assertEqual(response.status_code, 200)

    def test_update_url_view_post(self):
        updated_name = "Updated Site"
        data = {"name": updated_name, "url": "http://updatedsite.com"}
        response = self.client.post(
            reverse("vpn_service:update_url", args=[self.site.id]), data
        )
        self.site.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.site.name, updated_name)

    def test_delete_url_view_get(self):
        initial_count = Site.objects.filter(user=self.user).count()
        response = self.client.get(
            reverse("vpn_service:delete_url", args=[self.site.id])
        )
        updated_count = Site.objects.filter(user=self.user).count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(updated_count, initial_count - 1)

    def test_proxy_view_get_statistics(self):
        initial_count = SiteStatistics.objects.filter(user=self.user).count()
        response = self.client.get(
            reverse(
                "vpn_service:proxy_view", args=["Test Site", "www.example.com/page"]
            )
        )
        updated_count = SiteStatistics.objects.filter(user=self.user).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_count, initial_count + 1)

    def test_proxy_view_post_request(self):
        initial_count = SiteStatistics.objects.filter(user=self.user).count()
        response = self.client.post(
            reverse("vpn_service:proxy_view", args=["Test Site", "httpbin.org/post"])
        )
        updated_count = SiteStatistics.objects.filter(user=self.user).count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_count, initial_count + 1)
