import scrapy
from quotes_js_scraper.items import QuoteItem

from scrapy_splash import SplashRequest
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com']
    # start_urls = ['http://quotes.toscrape.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url='https://hackerone.com/reports/925513'
        yield SplashRequest(url, callback=self.parse)
        
    def parse(self, response):
        quote_item = QuoteItem()
        for item in response.css('div .report-card'):
            quote_item['author'] = item.css('div .interactive_markdown__p').get()
            yield quote_item