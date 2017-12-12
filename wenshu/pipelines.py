# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


# from googles.settings import COLLECTION_NAME


class MongoNewPipeline(object):
    def __init__(self, mongo_uri,mongo_db,collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection=collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_HOST'),  # localhost
            mongo_db=crawler.settings.get('MONGO_DB'),
            collection=crawler.settings.get('MONGO_COL')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]
        self.collection=self.db[self.collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item,spider):
        # self.db[self.collection].update({'key': item['key']}, dict(item), True)
        self.collection.insert(dict(item))
        return item

class WenshuPipeline(object):
    def process_item(self, item, spider):
        return item
