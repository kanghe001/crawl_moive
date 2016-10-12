# -*- coding: utf-8 -*-
import scrapy


class GetMoiveSpider(scrapy.Spider):
    name = "get_moive"
    start_urls = (
        'http://www.dytt8.net/',
    )

    def parse(self, response):
        pass
