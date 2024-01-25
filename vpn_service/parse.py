from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def process_static_content(soup, target_url):
    for tag in soup.find_all(["img", "script", "link"]):
        if "src" in tag.attrs:
            tag["src"] = urljoin(target_url, tag["src"])
        elif "href" in tag.attrs:
            tag["href"] = urljoin(target_url, tag["href"])


def process_links(soup, site_name, base_url):
    prefix = f"/{site_name}/{base_url}"

    for tag in soup.find_all("a"):
        href = tag.get("href", "")
        if not href.startswith(("http://", "https://", "www.")):
            tag["href"] = prefix + href


def parse_page(target_url):
    session = requests.Session()
    response = session.get(target_url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def send_post(request, target_url):
    csrf_token = request.COOKIES.get("csrftoken")

    post_data = request.POST.copy()
    post_data["csrftoken"] = csrf_token

    return requests.post(target_url, data=post_data)
