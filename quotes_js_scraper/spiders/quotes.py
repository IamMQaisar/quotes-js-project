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
        url='http://quotes.toscrape.com/js'
        yield SplashRequest(url, callback=self.parse)
        
    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item