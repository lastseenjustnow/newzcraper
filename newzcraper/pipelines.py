# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from pymongo import MongoClient
from pymongo.collection import Collection
from itemadapter import ItemAdapter


class MongoPipeline:

    collection_name = 'url_pages'

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
        self.collection_name.replace_one({'url': item['url']}, ItemAdapter(item).asdict(), upsert=True)
        return item
