import scrapy
from pathlib import Path

class WikiSpider(scrapy.Spider):
    name = "wiki"
    def start_requests(self):
        urls = [
        "https://quotes.toscrape.com/" # inital seed
        # https://en.wikipedia.org/wiki/Main_Page
        # "https://en.wikipedia.org/wiki/Elmvale_Acres_Shopping_Centre"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"Wiki-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        title= response.css("span::text").extract()# "span::mw-page-title-main"
        yield {"QUOTES ARE": title }

        link= response.css("li.next a::attr(href)").get()

        if link is not None:
            yield response.follow( link, callback= self.parse)