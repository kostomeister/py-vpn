from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from vpn_service.parse import (
    parse_page,
    process_static_content,
    process_links,
    send_post,
)


class ParseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_parse_page(self):
        soup = parse_page("http://example.com")
        self.assertIsNotNone(soup)

    def test_process_static_content(self):
        soup = BeautifulSoup('<img src="/image.jpg">', "html.parser")
        process_static_content(soup, "http://example.com")
        self.assertEqual(soup.find("img")["src"], "http://example.com/image.jpg")

    def test_process_links(self):
        soup = BeautifulSoup('<a href="/path/page.html">Link</a>', "html.parser")
        process_links(soup, "TestSite", "http://example.com")
        self.assertEqual(
            soup.find("a")["href"], "/TestSite/http://example.com/path/page.html"
        )
