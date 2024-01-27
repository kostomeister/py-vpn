import json
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class ContentProcessor:

    @staticmethod
    def get_soup(content):
        return BeautifulSoup(content, "html.parser")

    @staticmethod
    def process_static_content(soup, target_url):
        for tag in soup.find_all(["img", "script", "link", "form"]):
            if "src" in tag.attrs:
                tag["src"] = urljoin(target_url, tag["src"])
            elif "href" in tag.attrs:
                tag["href"] = urljoin(target_url, tag["href"])
            elif "action" in tag.attrs:
                tag["action"] = urljoin(target_url, tag["action"])

    @staticmethod
    def process_links(soup, site_name, base_url):
        prefix = f"/{site_name}/{base_url}"

        for tag in soup.find_all("a"):
            href = tag.get("href", "")
            if not href.startswith(("http://", "https://", "www.")):
                tag["href"] = prefix + href


class RequestHandler:
    def __enter__(self):
        self.client = requests.Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def send_get(self, target_url):
        return self.client.get(target_url)

    def send_post(self, data, target_url, csrf):
        cookies = {"csrftoken": csrf}
        header_info = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; SM-T535) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/83.0.4103.101 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "X-CSRFToken": csrf,
            "Referer": target_url,
        }
        data = json.dumps(data)
        response = self.client.post(target_url, data=data, headers=header_info, cookies=cookies)
        return response
