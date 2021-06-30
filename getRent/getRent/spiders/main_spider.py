import sys
import os
import scrapy
from getRent.items import House

# add the project directory to pythonpath so the spider can import from const.py file
def addToPath():
    path = os.getcwd()
    splitPath = path.split('/')
    constDirPath = '/'
    removeEmptySpace = splitPath[1:-3]
    separator = '/'
    constDirPath += separator.join(removeEmptySpace)
    sys.path.append(constDirPath)

addToPath()

from const import l_cities

class MainSpiderSpider(scrapy.Spider):
    count = 0
    name = 'main-spider'
    allowed_domains = ['https://www.apartments.com/denver-co/1-bedrooms/']
    start_urls = [f"https://www.apartments.com/{city}/1-bedrooms/{page}/" for city in l_cities for page in range(28)]

    def parse(self, response):
            
        rents = response.css('.price-range').css('::text').getall()
        addy = response.css('.js-url').css('::text').getall()
        zips = [addy[-5:] for a in addy]
        self.count += 1

        for i,rent in enumerate(rents):
            if type(addy[i]) == None:
                    ad = 'N/A'
            else:
                ad = addy[i]

            if type(zips[i]) == None:
                zi = 'N/A'
            else:
                zi = zips[i]


            if rent == 'Call for Rent' or type(rent) == None:
                re = 'N/A'
            else:
                re = rent

            
            yield House(name_id=self.count,zip_code=ad[-5:],price=re, address = ad)

