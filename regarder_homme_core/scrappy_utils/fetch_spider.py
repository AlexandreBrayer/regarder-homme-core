from typing import Union
from scrapy import spiderloader
from scrapy.utils import project
from scrapy.settings import default_settings 
from ..sites import *
from icecream import ic

ShopSpider = Union[TheBradery,CoolScrapper]

class Customsettings:
    def getlist(modules: str) -> str:
        return [TheBradery]

def fetch_spider(spider_name: str) -> ShopSpider:
    spider_loader = spiderloader.SpiderLoader(Customsettings)
    search = spider_loader.load(spider_name)
    return type(search)