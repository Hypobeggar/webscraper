# Webscraper
Core files:
wikiscraper/wikiscraper/spiders/wiki_spider.py
indexer.py
wikiscraper/processor.py

## Abstract
Webscraper consists of several python programs including a webcrawler, indexer, and query processor. The webcrawler is Scrapy based and is used to scrape Wikipedia tables of content. It also downloads the web documents in html format. The indexer uses Scikit-Learn and pickle to create an inverted index and serialize it respectively. The index has TF-IDF score representation and Cosine similarity. Webscraper's processor is Flask-based. It is used to handle json queries and provide the Top-K ranked results. Future endeavors consist of increasing the integration between the files. Currently, each program works individually. Eventually, you could index the results from the webscraping and process the data to query.

## Overview
The solution Webscraper provides are components consisting of a Scrapy-based webcrawler, Scikit-Learn based indexer, and Flask-based processor. Each component has a purpose and could connect with each other. The webcrawler can provide information crawled from the wikipedia website. The indexer can convert information, such as that provided by the crawler, into an inverted index. The processor could process information in a json format to be used for queries and ranking.

## Design
The webcrawler uses an initial seed, max pages, and max depth. AutoThrottle is utilized for concurrenet crawling. The crawler can be used to crawl websites for their html and Wikipedia for its table of contents. The html is saved to the current directory. The indexer uses Scikit-Learn to provide inverted index construction. Pickle is used to serialize and deserialize the constructed index. It provides a pickle file of the index in the current directory. Webscraper's processor can handle json data and be used to rank the data based on the similarity to the query. 

## Architecture
The main archictecture for Webscraper consists of Scrapy, Scikit-Learn, Pickle, and Flask. Other libraries used are Collections, NumPy, and Pathlib. They are used for  indexer, processor,and crawler, respectively. They serve important roles in the core features.

## Operation
### Installation
This repository can be forked and cloned for use. Webscraper is a python program, therefore python 3.11+ is required. The libraries consisting of Scrapy, Scikit-Learn, Pickle, Flask, Collections, NumPy, and Pathlib must be installed. The PowerShell file installs.ps1 can be used to install these dependencies.

### Usage
The wiki_spider.py can be run as is. The initial seed can also be changed to another Wikipedia article.
The file indexer.py can also be ran as is with the file.

The program processor.py can be ran as is but requires a command such as curl to receive results based on the query. The current set of data is found in the code. The following command is an example of this usage:
curl -X POST -H "Content-Type: application/json" -d '{"query": "fair"}' http://localhost:5000/query
Changing the value to the key/ value pair for "query" changes your query.

## Conclusion
Webscraper is currently separated in its features. Manual input is required for interaction between their functions. I was unable to create seamleass use between the components. However, each of the components work properly separately. When changed from Wikipedia articles, the portion of the crawler that searches the table of contents will prevent proper use.

## Data Sources
The only data sources are the information for the libraries. The library links are:
Scrapy- https://scrapy.org/ <br>
Scikit-Learn- https://scikit-learn.org/stable/index.html <br>
Pickle- https://docs.python.org/3/library/pickle.html <br>
Flask- https://flask.palletsprojects.com/en/3.0.x/ <br>
NumPy- https://numpy.org/ <br>
Pathlib- https://docs.python.org/3/library/pathlib.html <br>

## Test Cases
All data sources are held within the code. The base code and provided command(s) can be used as a test case.

## Source Code
The dependencies for Webscraper are Scrapy, Scikit-Learn, Pickle, Flask, Collections, NumPy, and Pathlib

## Bibliography
