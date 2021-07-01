# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
from scrapy.exporters import JsonItemExporter


class GetrentPipeline():

    file = None

    def open_spider(self, spider):
        time_now  = datetime.datetime.now().strftime('%m-%d-%Y') 
        file_name = f"House-{time_now}.json"
        self.file = open(file_name, 'wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# class GetrentPipeline:
#     def process_item(self, item, spider):
#         return item
