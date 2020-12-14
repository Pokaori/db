import scrapy


class LinksSpider(scrapy.Spider):
    name = "links"
    start_urls = [
        'https://student.apps.utah.edu/uofu/stu/ClassSchedules/main/1204/',
    ]

    def parse(self, response):
        for quote in response.css('div.col-lg-2'):
            yield {
                'link': quote.css('a::attr(href)').get(),
            }
