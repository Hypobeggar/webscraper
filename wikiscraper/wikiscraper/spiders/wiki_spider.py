import scrapy
from pathlib import Path

class WikiSpider(scrapy.Spider):
    name = "wiki"

    def start_requests(self):
        urls = [
            "https://en.m.wikipedia.org/wiki/Sadie_Houck"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f"Wiki-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        # Extract table of contents
        toc = response.xpath('//div[@id="toc"]') # AI agent ChatGPT

        if toc:
            yield {"table_of_contents": toc.extract()}

        # Follow links in the TOC if any
        for link in response.css("#toc a::attr(href)").getall():
            yield response.follow(link, callback=self.parse)
