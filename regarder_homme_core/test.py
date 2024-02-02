from scrapy import spiderloader
from scrapy.utils import project
from sites import TheBradery
# Manually specify spider modules
spider_modules = [TheBradery, "cool_scrapper"]

settings = project.get_project_settings()
spider_loader = spiderloader.SpiderLoader.from_settings(settings)
# Manually set the SPIDER_MODULES attribute
spider_loader.spider_modules = spider_modules
print(spider_loader.spider_modules)

# Specify the spider name
spider_name = "the_bradery"

# Load the spider class by name
spider_class = spider_loader.load(spider_name)

# Now you can access attributes and methods of the spider class without instantiating it
print("Spider Name:", spider_class.name)