# Webscraper
Core files:
wiki_spider.py, processor.py, indexer.py

## Abstract
Webscraper consists of several python programs including a webcrawler, indexer, and query processor. The webcrawler is Scrapy based and is used to scrape Wikipedia tables of content. It also downloads the web documents in html format. The indexer uses Scikit-Learn and pickle to create an inverted index and serialize it respectively. The index has TF-IDF score representation and Cosine similarity. Webscraper's processor is Flask-based. It is used to handle json queries and provide the Top-K ranked results. Future endeavors consist of increasing the integration between the files. Currently, each program works individually. Eventually, you could index the results from the webscraping and process the data to query.

## Overview
The solution Webscraper provides are components consisting of a Scrapy-based webcrawler, Scikit-Learn based indexer, and Flask-based processor. Each components has 

## Design
The webcrawler uses an initial seed, max pages, and max depth. AutoThrottle is utilized for concurrenet crawling. The indexer uses Scikit-Learn to provide inverted index construction. Pickle is used to serialize and deserialize the constructed index.
