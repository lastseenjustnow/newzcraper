import logging
import os

from pymongo import MongoClient
from pymongo import TEXT


u = os.environ['MONGO_ADMINUSERNAME']
p = os.environ['MONGO_ADMINPASSWORD']
db_name = os.environ['DB_NAME']
coll_name = os.environ['COLLECTION_NAME']

client = MongoClient('mongo', 27017, username=u, password=p)
db = client[db_name]
col = db[coll_name]
col.create_index([('category', TEXT), ('title', TEXT), ('text', TEXT)], name='text_search_index')
logging.info(f"Text search index has been created for db: {db_name}, collection: {coll_name}")
