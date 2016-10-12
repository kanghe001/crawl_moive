# -*- coding: utf-8 -*-
import scrapy


class GetMoiveSpider(scrapy.Spider):
    name = "get_moive"
    allowed_domains = ["http://www.dytt8.net/"]
    start_urls = (
        'http://www.http://www.dytt8.net//',
    )

    def parse(self, response):
        pass
