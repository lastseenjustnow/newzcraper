from datetime import datetime

from scrapy import Spider
from newzcraper.items import GuardianItem


class GuardianSpider(Spider):
    name = 'guardian'
    allowed_domains = ['theguardian.com']
    start_urls = [
        'https://www.theguardian.com/media/2021/jun/24/political-commentator-niki-savva-quits-the-australian-after-peta-credlin-joins-as-columnist',
        'https://www.theguardian.com/football/2021/jun/23/set-pieces-kane-and-covid-curveballs-the-big-issues-now-facing-england'
    ]

    def parse(self, response):
        for quote in response.css('div.dcr-1ipk5a'):
            item = GuardianItem()
            item['url'] = response.url,
            item['title'] = quote.xpath('//title/text()').extract()[0],
            item['author'] = quote.xpath('//a[@rel="author"]/text()').extract()[0],
            item['pub_date'] = quote.css('div.dcr-s64set label::text').get(),
            item['text'] = response.css('div.dcr-185kcx9 p::text').getall()
            item['insert_ts'] = datetime.now()
            yield item
