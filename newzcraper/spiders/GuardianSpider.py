from datetime import datetime
from itertools import chain

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from newzcraper.items import GuardianItem


class GuardianSpider(CrawlSpider):
    name = 'guardian'
    domain = 'www.theguardian.com'
    allowed_domains = [domain]
    start_urls = [
        'https://www.theguardian.com/'
    ]

    rules = (
        Rule(LinkExtractor(allow=('/[0-9]{4}/[a-z]{3}/[0-9]{1,2}/',), deny=['help', 'info'], unique=True),
             callback='parse',
             follow=False),
        Rule(LinkExtractor(allow=(domain,), deny=['help', 'info'], unique=False), follow=False)

    )

    def parse(self, response):
        self.logger.info('An article has been found at %s', response.url)

        for quote in response.css('div.dcr-1ipk5a'):
            item = GuardianItem()
            item['url'] = response.url
            item['category'] = response.url.split('/')[3]
            item['title'] = quote.xpath('//title/text()').extract()[0]
            item['author'] = quote.xpath('//a[@rel="author"]/text()').get()
            item['pub_date'] = quote.css('div.dcr-s64set label::text').get()
            item['text'] = ' '.join(chain(response.css('div.dcr-185kcx9 p::text').getall()))
            item['insert_ts'] = datetime.now()
            yield item
