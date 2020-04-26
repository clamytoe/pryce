#!/usr/bin/env python3
"""
app.py

Python Price Researcher
"""
import abc
import csv
from collections import namedtuple
from dataclasses import dataclass, field
from datetime import date
from typing import ClassVar, List

from bs4 import BeautifulSoup
import requests

from pryce.headers import FIREFOX_LINUX

Item = namedtuple("Item", "url img_url name price")


@dataclass
class Scraper(abc.ABC):
    search: str
    url: ClassVar[str]
    shop: ClassVar[str] = field(init=False)

    def __post_init__(self):
        self.search = self.search.strip().replace(' ', '+')
        self.scrape_shop()

    def make_request(self) -> BeautifulSoup:
        response = requests.get(f"{self.url}{self.search}", headers=FIREFOX_LINUX)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")

    @abc.abstractmethod
    def parse_item(self, soup, img=None) -> Item:
        pass

    @abc.abstractmethod
    def parse_page_items(self, soup) -> List[Item]:
        pass

    def save_to_csv(self, items: List[Item]) -> str:
        header = "url image name price".split()
        filename = f"{self.shop}_{date.today()}.csv"
        with open(filename, "w") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows([list(item) for item in items])
        return filename

    @abc.abstractmethod
    def scrape_shop(self):
        pass


@dataclass
class EbayScraper(Scraper):
    search: str
    url: ClassVar[str] = "https://www.ebay.com/sch/i.html?_nkw="
    shop: ClassVar[str] = "ebay"

    def parse_item(self, soup, img=None) -> Item:
        url = soup.find("a")["href"]
        img_url = soup.find("img", {"class": "s-item__image-img"})["src"]
        name = soup.find("h3", {"class": "s-item__title"}).text.strip()
        price = soup.find("span", {"class": "s-item__price"}).text.strip()
        return Item(url, img_url, name, price)

    def parse_page_items(self, soup) -> List[Item]:
        results = soup.find("ul", {"class": "srp-results"})
        items = results.find_all("li", {"class": "s-item"})
        return [self.parse_item(x) for x in items]

    def scrape_shop(self):
        soup = self.make_request()
        items = self.parse_page_items(soup)
        file_name = self.save_to_csv(items)
        print(f"{len(items)} items saved to {file_name}")


@dataclass
class BarnesScraper(Scraper):
    search: str
    url: ClassVar = "https://www.barnesandnoble.com/s/"
    shop: ClassVar = "barnesandnoble"

    def parse_item(self, soup, img=None) -> Item:
        site = f"https://www.{self.shop}.com"
        link_tag = soup.find("a", {"class": "link"})
        url = f"{site}{link_tag['href']}"
        name = link_tag["title"]
        price = link_tag.find_all("span")[-1].text.strip()
        img_url = f"https:{img.find('img')['src']}"
        return Item(url, img_url, name, price)

    def parse_page_items(self, soup) -> List[Item]:
        grid = soup.find("div", {"class": "product-shelf-grid"})
        images = grid.find_all("a", {"class": "pImageLink"})
        items = grid.find_all("div", {"class": "product-shelf-pricing"})
        return [self.parse_item(x, img) for x, img in zip(items, images)]

    def scrape_shop(self):
        soup = self.make_request()
        items = self.parse_page_items(soup)
        filename = self.save_to_csv(items)
        print(f"{len(items)} items saved to {filename}")


def main():
    scrapers = (BarnesScraper, EbayScraper)
    search = input("search term: ")
    if search:
        for scraper in scrapers:
            scraper(search)


if __name__ == "__main__":
    main()
