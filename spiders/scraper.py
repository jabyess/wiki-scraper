import scrapy
from scrapy.spiders import CrawlSpider

class LinkItem(scrapy.Item):
    href=scrapy.Field()
    text=scrapy.Field()

class WikiSpider(CrawlSpider):
    name = "wiki_spider"
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Special:Random']

    followed_links = []

    def parse(self, response):
        all_links = response.css('.mw-parser-output p a')

        for link in all_links:
            text = link.css('::text').get()
            href = link.css('::attr(href)').get()
            item = LinkItem(text=text, href=href)
            
            if len(text) > 1 and text[0].islower():
                print({'link':text})
                self.followed_links.append(item)

                return response.follow(href, self.parse)
        
        print(self.followed_links)

