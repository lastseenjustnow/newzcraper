import logging
from newzcraper.spiders import GuardianSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    from mongo import crud

    process = CrawlerProcess(get_project_settings())

    process.crawl(GuardianSpider.GuardianSpider)
    process.start()
