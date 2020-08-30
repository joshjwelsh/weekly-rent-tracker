import scrapy
from getRent.items import House

class MainSpiderSpider(scrapy.Spider):
    l_cities = [
    'newyork - ny',
    'los-angeles-ca',
    'san-francisco-ca',
    'denver-co',
    'washington-dc',
    'miami-fl',
    'chicago-il',
    'dallas-tx',
    'austin-tx',
    'boulder-co'
    ]
    count = 0
    name = 'main-spider'
    allowed_domains = ['https://www.apartments.com/denver-co/1-bedrooms/']
    start_urls = [f"https://www.apartments.com/{city}/1-bedrooms/{page}/" for city in l_cities for page in range(28)]

    def parse(self, response):
            
        rents = response.css('.altRentDisplay').css('::text').getall()
        addy = response.css('.location').css('::text').getall()
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

