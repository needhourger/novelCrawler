# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bid = scrapy.Field()
    bname = scrapy.Field()
    author = scrapy.Field()
    btype = scrapy.Field()
    url = scrapy.Field()
    lastUpdate = scrapy.Field()
    total_chapters = scrapy.Field()
    download_chapters = scrapy.Field()

