# Webscraper

## Abstract
Webscraper consists of several python programs including a webcrawler, indexer, and query processor. The webcrawler is Scrapy based and is used to scrape Wikipedia tables of content. It also downloads the web documents in html format. The indexer uses Scikit-Learn and pickle to create an inverted index and serialize it respectively. The index has TF-IDF scores and Cosine similarity. Webscraper's processor is Flask-based. It is used to handle json queries and provide the Top-K ranked results. Future endeavors consist of increasing the integration between the files. Currently, each program works individually. Eventually, you could index the results from the webscraping and process the data to query.
