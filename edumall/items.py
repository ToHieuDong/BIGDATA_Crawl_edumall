# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EdumallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    TenKhoaHoc = scrapy.Field()
    GiangVien = scrapy.Field()
    Title = scrapy.Field()
    MoTa = scrapy.Field()
    Gia = scrapy.Field()
    
