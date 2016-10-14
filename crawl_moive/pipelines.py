# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib


class CrawlMoivePipeline(object):

    def process_item(self, item, spider):
        urllib.urlretrieve(item["moive_url"], "./heheda.mp4")
        return item
