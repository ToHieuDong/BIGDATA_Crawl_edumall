import scrapy
import json
from edumall.items import EdumallItem

class EduSpider(scrapy.Spider):
    name = "edu"
    allowed_domains = ["edumall.vn"]
    start_urls = ["https://edumall.vn/khoa-hoc"]

    def parse(self, response):
        links = []
        for i in range(3):
            s = "https://edumall.vn/khoa-hoc?page=" + str(i+1)
            links.append(s)

        for link in links:
            yield scrapy.Request(link, callback=self.parse_detail)

    def parse_detail(self, response) :
        items = []
        for i in range (10) :
            item = EdumallItem() 
            item['TenKhoaHoc'] = response.xpath('//div[@id="emCatCrsCardRsv'+str(i+1)+'"]/button/div[2]/div[1]/text()').get()
            item['Title'] = response.xpath('//div[@id="emCatCrsCardRsv'+str(i+1)+'"]/button/div[2]/h6/text()').get()
            item['MoTa'] = response.xpath('//div[@id="emCatCrsCardRsv'+str(i+1)+'"]/button/div[2]/p/text()').get()
            item['GiangVien'] = response.xpath('//div[@id="emCatCrsCardRsv'+str(i+1)+'"]/button/div[2]/div[2]/text()').get()
            items.append(item)
        
        yield items

        with open('output.json', 'a', encoding='utf-8') as json_file:
            for item  in items :
                json.dump(dict(item), json_file, ensure_ascii=False)
                json_file.write('\n')


        




        
