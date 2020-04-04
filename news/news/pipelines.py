# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class NewsPipeline(object):
    def __init__(self):
        self.file = open('news163_data.csv', 'wb')  # 打开文件
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')  # 实例化CSV模块
        self.exporter.start_exporting()  # 开始导出

    def close_spider(self, spider):
        # 结束导出并关闭文件
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        # 导出进程
        self.exporter.export_item(item)
        return item
