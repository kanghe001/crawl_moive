# -*- coding: utf-8 -*-
import scrapy


class GetMoiveSpider(scrapy.Spider):
    name = "get_moive"
    start_urls = (
        'http://www.bilibili.com/video/av6623541/',
    )

    def __init__(self):
        super(GetMoiveSpider, self).__init__(self)

        # use any browser you wish
        self.browser = webdriver.Firefox()

    def __del__(self):

        self.browser.close()

    def parse(self, response):
        moive = response.css(".bilibili-")
