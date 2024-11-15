import datetime
import os
import unicodedata

import requests
from bs4 import BeautifulSoup


def get_pdf(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Skipping {url}: 404 Not Found")
        else:
            raise


def scraping(year: int):
    last_year = datetime.datetime.now().year - 1
    link = "index" if year == last_year else year
    url = f"https://www.oit.ac.jp/inside/jugyou_anq/{link}.html"
    print(f"Scraping {url}")
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.content, "html.parser")
    links = soup.find_all("a", href=True)
    pdf_url = "https://www.oit.ac.jp/inside/jugyou_anq/"
    os.makedirs(f"data/{year}", exist_ok=True)

    for link in links:
        if link["href"].startswith("pdf/"):
            pdf_link = link["href"]
            term = "前期" if pdf_link.split("/")[-2] == "zenki" else "後期"
            faculty = unicodedata.normalize("NFKC", link.find_previous("th").get_text(strip=True))
            department = unicodedata.normalize("NFKC", link.get_text(strip=True))
            filename = os.path.join("data", str(year), f"{term}-{faculty}-{department}.pdf")
            path = pdf_url + pdf_link
            print(f"Downloading {path} as {filename}")
            get_pdf(path, filename)


if __name__ == "__main__":
    import sys

    scraping(int(sys.argv[1]))
