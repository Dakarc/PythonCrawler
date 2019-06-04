# -*- coding: utf-8 -*-
import scrapy


class QsbkdemoSpider(scrapy.Spider):
    name = 'qsbkdemo'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/text/page/1']

    def parse(self, response):
       duanzidivs = response.xpath("//div[@id='content-left']/div")
       for duanzidiv in duanzidivs:
           author = duanzidiv.xpath(".//h2/text()").get().strip()
           content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
           content = "".join(content).strip()
           duanzi = {"author":author,"content":content}
           yield duanzi