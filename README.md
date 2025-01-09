# Wiki Scraper 

I don't have a better name

## what

An experiment using `scrapy` and `flask`.

## Motivation

There's a trope that if you start with a [random article](https://en.wikipedia.org/wiki/Special:Random), click the first *lowercase* link, and continue to follow that pattern, you will eventually wind up at [Philosophy](https://en.wikipedia.org/wiki/Philosophy).

So I wanted to build a thing that would visualize this in a graph of all the links visited.

## run it
- have pipenv
- install dependencies: `pipenv install` 
- activate virtual environment: `pipenv shell`
- run scraper: `scrapy runspider wikiscraper/spiders/wiki.py`