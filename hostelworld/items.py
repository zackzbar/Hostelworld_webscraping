# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HostelworldItem(scrapy.Item):
    kind = scrapy.Field()
    distance = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    rating_cat = scrapy.Field()
    reviews = scrapy.Field()
    value_for_money = scrapy.Field()
    security = scrapy.Field()
    location = scrapy.Field()
    staff = scrapy.Field()
    atmosphere = scrapy.Field()
    cleanliness = scrapy.Field()
    facilities = scrapy.Field()
    description = scrapy.Field()
    free = scrapy.Field()
    # general = scrapy.Field()
    # services = scrapy.Field()
    # food_drink = scrapy.Field()
    # entertainment = scrapy.Field()
