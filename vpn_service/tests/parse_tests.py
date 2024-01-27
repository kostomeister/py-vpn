from bs4 import BeautifulSoup
from django.test import RequestFactory, TestCase
from vpn_service.parse import (
    ContentProcessor,
    RequestHandler,
)


class ParseTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_parse_page(self):
        with RequestHandler() as handler:
            response = handler.send_get("http://example.com")
            soup = ContentProcessor.get_soup(response.content)
            self.assertIsNotNone(soup)

    def test_process_static_content(self):
        soup = BeautifulSoup('<img src="/image.jpg">', "html.parser")
        ContentProcessor.process_static_content(soup, "http://example.com")
        self.assertEqual(soup.find("img")["src"], "http://example.com/image.jpg")

    def test_process_links(self):
        soup = BeautifulSoup('<a href="/path/page.html">Link</a>', "html.parser")
        ContentProcessor.process_links(soup, "TestSite", "http://example.com")
        self.assertEqual(
            soup.find("a")["href"], "/TestSite/http://example.com/path/page.html"
        )
