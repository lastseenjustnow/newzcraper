import os

from scrapy import Spider


class GuardianSpider(Spider):
    name = 'guardian'
    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/au']

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'guardian-{page}.html'
        with open(os.path.join('_tmp_html', filename), 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
