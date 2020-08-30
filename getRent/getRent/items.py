# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class House(scrapy.Item):
    name_id = scrapy.Field()
    zip_code = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    


