from scrapy import Spider, Request
from hostelworld.items import HostelworldItem
import re
import math

class HostelworldSpider(Spider) :
    name = 'hostelworld_spider'
    allowed_urls = ['https://www.hostelworld.com']
    start_urls =    ['https://www.hostelworld.com/hostels/Hanoi/Vietnam', 
                     # 'https://www.hostelworld.com/hostels/Bangkok/Thailand',
                     # 'https://www.hostelworld.com/hostels/Ho-Chi-Minh/Vietnam',
                     # 'https://www.hostelworld.com/hostels/Hoi-An/Vietnam',
                     # 'https://www.hostelworld.com/hostels/Da-Nang/Vietnam',
                     'https://www.hostelworld.com/hostels/Hue/Vietnam']

    def parse(self, response) :
        num = int(response.xpath('//span[@class="numPropertiesReturnedFromSearch"]/text()').extract_first())
        num = math.ceil(num/30)

        num_pages = [f'?page={i+1}' for i in range(num)]

        result_urls = []
        for x in self.start_urls:
            for y in num_pages:
                result_urls.append(x + y)

        print('='*55)
        print(len(result_urls))
        print(result_urls)
        print('='*55)

        for url in result_urls:
            yield Request(url=url, callback=self.parse_results_page)



    def parse_results_page(self, response) :
        hostel_urls = response.xpath('//a[@class="hwta-property-link"]/@href').extract()
        hostel_urls = list(set(hostel_urls))[1:]

        print('='*55)
        print(len(hostel_urls))
        print('='*55)

        for url in hostel_urls:
            yield Request(url=url, callback=self.parse_hostel_page)

    def parse_hostel_page(self, response) :
        
        # kind = 

        # distance = 

        # private = 

        # dorm = 

        city = response.xpath('//span[@class="adddress"]/a[2]/text()').extract_first()
        print('='*55)
        print(city)
        print('='*55)

        country = response.xpath('//span[@class="adddress"]/a[3]/text()').extract_first()

        name = response.xpath('//h1[@class="main-title"]/@data-name').extract_first()
        print('='*55)
        print(name)
        print('='*55)

        try:
            place1 = response.xpath('//div[@class="ms-rating-summary-block"]//div[@class="score"]/text()').extract_first()
            rating = re.findall('[0-9]*\.?[0-9]', place1)[0]
        except:
            rating = ""

        try:
            rating_cat = response.xpath('//div[@class="ms-rating-summary-block"]//p[@class="keyword"]/text()').extract_first()
        except:
            rating_cat = ""

        try:
            place2 = response.xpath('//div[@class="ms-rating-summary-block"]//span/text()').extract_first()
            reviews = re.findall('\d+', place2)[0]
        except:
            reviews = ""

        try:
            value_for_money = response.xpath('//ul[@class="row rating-breakdown"]//li[1]//strong/text()').extract_first()
        except:
            value_for_money = ""

        try:
            security = response.xpath('//ul[@class="row rating-breakdown"]//li[2]//strong/text()').extract_first()
        except:
            security = ""

        try:
            location = response.xpath('//ul[@class="row rating-breakdown"]//li[3]//strong/text()').extract_first()
        except:
            location = ""

        try:
            staff = response.xpath('//ul[@class="row rating-breakdown"]//li[4]//strong/text()').extract_first()
        except:
            staff = ""

        try:
            atmosphere = response.xpath('//ul[@class="row rating-breakdown"]//li[5]//strong/text()').extract_first()
        except:
            atmosphere = ""

        try:
            cleanliness = response.xpath('//ul[@class="row rating-breakdown"]//li[6]//strong/text()').extract_first()
        except:
            cleanliness = ""

        try:
            facilities = response.xpath('.//ul[@class="row rating-breakdown"]//li[7]//strong/text()').extract_first()
        except:
            facilities = ""

        # free = 

        # general = 

        # services = 

        # food_drink = 

        # entertainment = 


        item = HostelworldItem()
        # item['kind'] = kind
        # item['distance'] = distance
        # item['private'] = private
        # item['dorm'] = dorm
        item['city'] = city
        item['country'] = country
        item['name'] = name
        item['rating'] = rating
        item['rating_cat'] = rating_cat
        item['reviews'] = reviews
        item['value_for_money'] = value_for_money
        item['security'] = security
        item['location'] = location
        item['staff'] = staff
        item['atmosphere'] = atmosphere
        item['cleanliness'] = cleanliness
        item['facilities'] = facilities
        # item['free'] = free
        # item['general'] = general
        # item['services'] = services
        # item['food_drink'] = food_drink
        # item['entertainment'] = entertainment

        yield item




