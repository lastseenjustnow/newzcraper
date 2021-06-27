from datetime import datetime
from itertools import chain

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from newzcraper.items import GuardianItem
from readability.cleaners import normalize_spaces


class GuardianSpider(CrawlSpider):

    """
    This class implements crawling through www.theguardian.com and parsing articles.
    An article is detected in case it has a date specifically formatted in the link.
    """

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

        """
        This function attempts to recognize an article and extract needed data using predefined tags.
        Tags are specifically set, could be created more generic solution for various types of news sites.

        :param response: response from media web service
        :return: generator of documents
        """

        self.logger.info('An article has been found at %s', response.url)

        for quote in response.css('div.dcr-1ipk5a'):
            item = GuardianItem()
            item['url'] = response.url
            item['category'] = response.url.split('/')[3]
            item['title'] = quote.xpath('//title/text()').extract()[0]
            item['author'] = quote.xpath('//a[@rel="author"]/text()').get()
            item['pub_date'] = quote.css('div.dcr-s64set label::text').get()
            item['text'] = normalize_spaces(' '.join(chain(response.css('div.dcr-185kcx9 p::text').getall())))
            item['insert_ts'] = datetime.now()
            yield item
