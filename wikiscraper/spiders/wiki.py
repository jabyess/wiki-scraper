import scrapy
from scrapy import signals

class LinkItem(scrapy.Item):
    href=scrapy.Field()
    text=scrapy.Field()

class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/St_David%27s_Hospital,_Carmarthen"]

    followed_links = []

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = super(WikiSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider

    def parse(self, response):
        all_links = response.css('#mw-content-text p a')

        # for link in reversed(all_links):
        for link in all_links:
            text = link.css('::text').get()
            href = link.css('::attr(href)').get()
            item = LinkItem(text=text, href=href)

            if "Philosophy" in href:
                return 

            if len(text) > 1 and text[0].islower():
                self.followed_links.append(item)
                self.logger.info(f"added item {item}")

                return response.follow(href, self.parse)

    def closed(self, spider):
        self.logger.info(f"-----------all links-------------{self.followed_links}")
        terms = []
        for item in self.followed_links:
            terms.append(f"{item.get('text')} ")
        self.logger.info(terms)
            
