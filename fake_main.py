
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy import spiderloader

def main():
# Get the project settings
    settings = get_project_settings()

    process = CrawlerProcess(settings)

    # Create a SpiderLoader
    spider_loader = spiderloader.SpiderLoader.from_settings(settings)

    print(spider_loader.spider_modules)
    spider_names = ["the_bradery"]

    # Load and run each spider
    for spider_name in spider_names:
        # Load the spider class by name
        spider_class = spider_loader.load(spider_name)
        print("Spider Name:", spider_class.name)
        # Schedule the spider for running
        # process.crawl(spider_class)

main()