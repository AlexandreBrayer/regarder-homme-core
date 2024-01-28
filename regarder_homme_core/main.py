from scrapy.crawler import CrawlerProcess
from .sites.the_bradery import TheBradery

def main():
    process = CrawlerProcess()
    process.crawl(TheBradery)
    process.start()