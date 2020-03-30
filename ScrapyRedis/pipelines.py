# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class MongodbPipeline(object):

	def __init__(self):
		self.host = '127.0.0.1'
		self.port = 27017
		self.mongodb = 'Trip'  # 库
		self.mongo_table = 'Chengdu'  # 集合
		self.mongo_table2 = 'Chengdu2'  # 集合2(存储没有照片评论的景点)
		self.client = pymongo.MongoClient(host=self.host, port=self.port)  # 建立链接

		self.db = self.client[self.mongodb]  # 连接库
		self.tb = self.db[self.mongo_table]  # 操作集合
		self.tb2 = self.db[self.mongo_table2]  # 操作集合2

	def __del__(self):
		self.client.close()

	def process_item(self, item, spider):
		if item['intro'] == '' and item['comment'] == '':
			# self.tb2.insert_one(item)
			# print('Successful Save Message To t2')
			self.tb.update({'link': item['link']}, {'$set': {'name': item['name'], 'en_name': item['en_name'],
															 'photo': item['photo'],'intro': item['intro'],
															 'address': item['address'], 'comment': item['comment'], 'opentime': item['opentime']}}, True)
		else:
			# self.tb.insert_one(item)  # check_keys=False 不检测key，防止特殊字符 例.
			# print('Successful Save Message To t1')
			self.tb.update({'link': item['link']}, {'$set': {'name': item['name'], 'en_name': item['en_name'],
															 'photo': item['photo'],'intro': item['intro'],
															 'address': item['address'], 'comment': item['comment'], 'opentime': item['opentime']}}, True)
			print('Successful Save Message To t1')


# documents must have only string keys, key was 0  存储数据中不能有bytes只能是字符串
