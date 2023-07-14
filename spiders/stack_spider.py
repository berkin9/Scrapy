import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.item import StackItem
from pathlib import Path

class StackSpider(Spider):
    name = "stack"
    allowed_domains = [""]
    start_urls = [
        "https://www.kitapyurdu.com/kategori/kitap/1.html",
    ]
    

    def parse(self, response):
        books = response.css('div.product-cr')

        for book in books:
            item = StackItem()
            yield{
                item['title'] : book.css('.name a span::text').get(),
                item['price']: book.css('.price .price-new span.value::text').get(),  
                item['author']: book.css('.author span a span::text').get(),
                item['publisher'] : book.css('.publisher span a span::text').get(),   
            }

