from scrapy import Request
import json
from ..product_description import Product, ProductSpider

SITE_NAME = "the_bradery"
START_URLS = ["https://thebradery.com/collections"]


class TheBradery(ProductSpider):
    def __init__(self):
        super().__init__()

    name = SITE_NAME
    start_urls = START_URLS

    def parse(self, response: Request):
        ahrefs = response.css("a::attr(href)").extract()
        paths = [x for x in ahrefs if x.startswith("/collections/")]
        paths = list(set(paths))
        for path in paths:
            yield Request(
                response.urljoin(
                    path + "/products.json?view=metafields&limit=100000&page=1"
                ),
                callback=self.parse_category,
            )

    def parse_category(self, response: Request):
        products = json.loads(response.body)
        for product in products["products"]:
            for sku in product["variants"]:
                if sku["sku"] != "" and sku["sku"] is not None:
                    self.products.append(
                        Product(
                            title=product["title"],
                            url="https://thebradery.com/products/" + product["handle"],
                            reference=sku["sku"],
                            # rrp=float(
                            #     product["variants"][0]["compare_at_price"]
                            #     or product["variants"][0]["price"]
                            # ),
                            price=float(product["variants"][0]["price"]),
                            currency="EUR",
                            # category=product["product_type"],
                            # brand=product["vendor"],
                            # description= product["body_html"],
                            # images_url= [x["src"] for x in product["images"]],     
                        )
                    )
