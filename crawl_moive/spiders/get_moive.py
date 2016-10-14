# -*- coding: utf-8 -*-
import scrapy
from crawl_moive.items import CrawlMoiveItem


class GetMoiveSpider(scrapy.Spider):
    name = "get_moive"
    start_urls = (
        'http://lol.qq.com/v/',
    )

    def __init__(self):
        super(GetMoiveSpider, self).__init__(self)
        pass

    def parse(self, response):
        item = CrawlMoiveItem()
        item['moive_url'] = response.css(".top-big-video source::attr(src)").extract()[1]
        yield item
