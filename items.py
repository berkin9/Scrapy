# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
class StackItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field()
    price = Field()
    author = Field()
    publsiher = Field()

    # name = scrapy.Field()
    pass
