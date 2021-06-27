from typing import List, Dict
import os
import re

from pymongo import MongoClient

environ_vars = ['MONGO_ADMINUSERNAME', 'MONGO_ADMINPASSWORD', 'DB_NAME', 'COLLECTION_NAME']
default_u, default_p, default_db_name, default_coll_name = (os.environ[env_name] for env_name in environ_vars)


class MongoToFlask:

    """This class implements interaction methods between MongoDB and the backend."""

    def __init__(self, u=default_u, pwd=default_p, h='mongo', port=27017,
                 db_name=default_db_name,
                 coll_name=default_coll_name):
        self.username = u
        self.password = pwd
        self.hostname = h
        self.port = port
        self.client = MongoClient(
            self.hostname,
            27017,
            username=self.username,
            password=self.password)
        self.db = self.client[db_name]
        self.col = self.db[coll_name]

    def list_databases(self):
        db_list = [db for db in self.client.list_database_names()]
        return db_list

    def search_by_keyword(self, keyword: str) -> List[Dict]:

        """
        This method is called to search a database by a keyword.
        It employs MongoDB query language. Could be rewritten using jsons, serializable classes etc. depending on the demand of the project
        :param keyword: a word to be searched by in the database
        :return: a list of dicts containing document items filtered
        """

        cursor = self.col.find(
            {"$text": {"$search": keyword}},
            {"url": 1, "category": 1, "text": 1, "_id": 0}
        )

        def cut_context(txt, word, letters_number):
            """
            This is an auxiliary function for a keyword context discovery

            :param txt: a string containing text
            :param word: a keyword set for searching the context
            :param letters_number: an amount of letters to display from both sides of the keyword
            :return: context string
            """
            if re.search(word, txt):
                index = re.search(word, txt).start()
            else:
                return None
            context = txt[max(0, index - letters_number): index + letters_number]
            return '...' + ''.join(context) + '...'

        docs: List[Dict] = [
            dict(map(lambda x: (x[0], cut_context(x[1], keyword, 100) if x[0] == 'text' else x[1]), doc.items()))
            for doc in cursor]

        return docs
