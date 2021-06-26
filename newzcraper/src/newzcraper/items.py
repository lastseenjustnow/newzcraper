# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuardianItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    pub_date = scrapy.Field()
    text = scrapy.Field()
    insert_ts = scrapy.Field()

    def __repr__(self):
        """only print out title after exiting the Pipeline"""
        return repr({"title": self['title']})
