# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ScrapyredisItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    en_name = Field()
    address = Field()
    photo = Field()
    intro = Field()  # 描述
    comment = Field()  # 评论
    opentime = Field()  # 开放时间
    _id = Field()
    link = Field()
    # name = Field()
    # name = Field()
    # name = Field()




