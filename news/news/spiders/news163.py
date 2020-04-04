# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import NewsItem


class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://news.163.com/20/0403/\d+/.*?html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NewsItem()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        item['news_thread'] = response.url.strip().split('/')[-1][:-5]
        self.get_title(response, item)
        self.get_time(response, item)
        self.get_source(response, item)
        self.get_source_url(response, item)
        self.get_text(response, item)
        self.get_url(response, item)
        return item

    def get_title(self, response, item):
        title = response.css('title::text').extract()
        if title:
            print('title is {}'.format(title[0][:-5]))
            item['news_title'] = title[0][:-5]

    def get_time(self, response, item):
        time = response.css('div.post_time_source::text').extract()
        if time:
            print('time is {}'.format(time[0].strip().replace('来源:', '').replace('\u3000', '')))
            item['news_time'] = time[0].strip().replace('来源:', '').replace('\u3000', '')

    def get_source(self, response, item):
        source = response.css('#ne_article_source::text').extract()
        if source:
            print('source is {}'.format(source[0]))
            item['news_source'] = source[0]

    def get_source_url(self, response, item):
        source_url = response.css('#ne_article_source::attr(href)').extract()
        if source_url:
            print('source url is {}'.format(source_url[0]))
            item['source_url'] = source_url[0]

    def get_text(self, response, item):
        text = response.css('.post_text p::text').extract()
        if text:
            item['news_body'] = text

    def get_url(self, response, item):
        url = response.url
        if url:
            item['news_url'] = url  # 每个url爬取过都储存起来
