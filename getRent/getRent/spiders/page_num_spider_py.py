import scrapy


class PageNumSpiderPySpider(scrapy.Spider):
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
    name = 'page_num_spider.py'
    allowed_domains = ['apartments.com/{city}/1-bedrooms/1/']
    start_urls = ['http://apartments.com/{city}/1-bedrooms/'.format(city=city) for city in l_cities]

    def parse(self, response):
        page_count = response.css('.pageRange').css('::text').getall()
        for page in page_count:
            yield {'num':page}