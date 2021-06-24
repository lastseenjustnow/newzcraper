import logging
import os

from pymongo import MongoClient

logging.info("Initializing MongoDB Client...")

u = os.environ['MONGO_ADMINUSERNAME']
p = os.environ['MONGO_ADMINPASSWORD']
client = MongoClient('mongo', 27017, username=u, password=p)

for db in client.list_databases():
    logging.info(db)
