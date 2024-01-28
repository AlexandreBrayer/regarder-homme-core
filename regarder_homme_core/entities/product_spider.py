import scrapy
import json
from pydispatch import dispatcher
from scrapy import signals
import sys
from typing import TypeVar

from . import Product

T = TypeVar("T")

def convert_product(products: list[Product]) -> dict[str,T]:
    return [vars(product) for product in products]

class ProductSpider(scrapy.Spider):
    def __init__(self)-> None:
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.products = []
        
    def spider_closed(self, spider: scrapy.Spider)-> None:
        stats = self.crawler.stats.get_stats()
        self.products = convert_product(self.products)
        print(json.dumps(
            {"products": self.products, "stats": stats, "spider_name": spider.name}, default=str))
        sys.stdout.flush()

