import json
from pydispatch import dispatcher
from scrapy import Spider, signals
import sys
from typing import TypeVar

from . import Product

T = TypeVar("T")

def convert_product(products: list[Product]) -> dict[str,T]:
    return [vars(product) for product in products]

class ProductSpider(Spider):
    def __init__(self)-> None:
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.products = []
        
    def spider_closed(self, spider: Spider)-> None:
        stats = self.crawler.stats.get_stats()
        self.products = convert_product(self.products)
        print(json.dumps(
            {"products": self.products, "stats": stats, "spider_name": spider.name}, default=str))
        sys.stdout.flush()
