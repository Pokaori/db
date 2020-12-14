import scrapy
import json

with open('links.json', 'r') as f:
    links = json.loads(f.read())

class LinksSpider(scrapy.Spider):
    name = "subjects"
    start_urls = [ 'https://student.apps.utah.edu/uofu/stu/ClassSchedules/main/1204/'+ link["link"] for link in links]

    def parse(self, response):
        for quote in response.css('div.card-body h3'):
            yield {
                'subject': quote.css('span::text').getall()[1],
            }
