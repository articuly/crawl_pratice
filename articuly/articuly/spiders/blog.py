# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticulyItem


class BlogSpider(CrawlSpider):
    name = 'blog'
    allowed_domains = ['articuly.com']
    start_urls = ['http://articuly.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://articuly.com/\w+\-.*?/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ArticulyItem()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        self.get_title(response, item)
        self.get_url(response, item)
        self.get_time(response, item)
        self.get_tags(response, item)
        self.get_content(response, item)
        return item

    def get_title(self, response, item):
        title = response.css('.entry-title::text').extract()
        if title:
            print('title is {}'.format(title[0]))
            item['blog_title'] = title[0]

    def get_url(self, response, item):
        url = response.url
        if url:
            print('url is {}'.format(response.url))
            item['blog_url'] = response.url

    def get_time(self, response, item):
        time = response.css('span.updated::text').extract()
        if time:
            print('time is {}'.format(time[0]))
            item['blog_time'] = time[0]

    def get_tags(self, response, item):
        tag = response.css('.meta-tags a::text').extract()
        if tag:
            print('tag is {}'.format(tag))
            item['blog_tags'] = tag

    def get_content(self, response, item):
        content = response.css('.post-content p::text').extract()
        if content:
            print('content is {}'.format(content))
            item['blog_content'] = content
