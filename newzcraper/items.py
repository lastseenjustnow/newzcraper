# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuardianItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    pub_date = scrapy.Field()
    text = scrapy.Field()