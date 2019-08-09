# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DLFileItem(scrapy.Item) :
    
    sub_dir = scrapy.Field()

    file_urls = scrapy.Field()
    file = scrapy.Field()