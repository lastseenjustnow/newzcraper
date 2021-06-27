# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

from pymongo import MongoClient
from pymongo.collection import Collection
from itemadapter import ItemAdapter


class MongoPipeline:
    """
    This class implements functionality for preprocessing scraped data & sending it to MongoDB.
    """

    collection_name = os.environ['COLLECTION_NAME']

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB', 'items')
        )

    def open_spider(self, spider):
        self.client: MongoClient = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection_name: Collection = self.db[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        This method defines a strategy for database population.
        Replacement is used here to avoid duplicates in the db, another approach that could be applied -
        to create an index for url in a database level. In this case exceptions must be handled properly.
        """
        self.collection_name.replace_one({'url': item['url']}, ItemAdapter(item).asdict(), upsert=True)
        return item
