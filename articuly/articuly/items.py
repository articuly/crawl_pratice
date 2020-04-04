# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticulyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    blog_title = scrapy.Field()
    blog_url = scrapy.Field()
    blog_time = scrapy.Field()
    blog_tags = scrapy.Field()
    blog_content = scrapy.Field()
