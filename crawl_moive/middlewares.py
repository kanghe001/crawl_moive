# !/usr/bin/env python
# coding=utf-8


import scrapy
import random
from crawl_moive.settings import agents
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class CrawlMoiveUserAgent(UserAgentMiddleware):

    # @classmethod
    # def from_crawler(cls, crawler):
    #    self.agents =

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(agents))
