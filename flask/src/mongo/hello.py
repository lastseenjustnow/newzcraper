import logging
import os

from pymongo import MongoClient


def list_databases():
    u = os.environ['MONGO_ADMINUSERNAME']
    p = os.environ['MONGO_ADMINPASSWORD']
    client = MongoClient('mongo', 27017, username=u, password=p)

    db_list = [db for db in client.list_database_names()]
    return db_list
