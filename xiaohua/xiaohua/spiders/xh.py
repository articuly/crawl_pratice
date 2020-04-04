# -*- coding: utf-8 -*-
import scrapy


class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohua.zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/new/1.html',
                  'http://xiaohua.zol.com.cn/new/2.html',
                  'http://xiaohua.zol.com.cn/new/3.html',
                  'http://xiaohua.zol.com.cn/new/4.html',
                  'http://xiaohua.zol.com.cn/new/5.html', ]

    def parse(self, response):
        page = response.url.split('/')[-1][-6]
        filename = 'xiaohua-{}.txt'.format(page)
        title = response.xpath('//html/head/title/text()').extract()
        print('title is', title)
        with open(filename, 'w') as f:
            jokes = response.css('li.article-summary')
            for joke in jokes:
                joke_title = joke.css('.article-title a::text').extract()[0]
                joke_source = joke.css('.article-source span::text').extract()[-1]
                joke_content = joke.css('.summary-text p::text').extract()
                print(joke_title)
                print(joke_source)
                print(joke_content)
                f.write(f'{joke_title}\t{joke_source}\t{joke_content}\n')
