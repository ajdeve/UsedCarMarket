import scrapy
# text cleaning
import re
class ScrapeTableSpider(scrapy.Spider):
    name = "extract"
    start_urls = ['https://www.iseecars.com/car/2017-acura-ilx']

    def start_requests(self):
        with open("urls.csv") as f:
            urls = []
            for line in f:
                columns = line.split(",")
                for i in columns:
                    i = i.rstrip('\n')
                    urls.append(i)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.css('.table3 tr'):
            yield {
                'Url': response.request.url,
                'Type': row.xpath('th[1]//text()').extract_first(),
                'Trim': row.xpath('td[2]//text()').extract_first(),
                'Style': row.xpath('td[3]//text()').extract_first(),
                'Engine': row.xpath('td[4]//text()').extract_first(),
                'Drive Train': row.xpath('td[5]//text()').extract_first(),
                'MSRP': row.xpath('td[6]//text()').extract_first()
            }
              