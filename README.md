# chewy-seo

This repo is about practices to extract product attributes from Amazon pet supplies reviews, and score customers' opinions per attribute per product. Please download origin datasets [here:](http://jmcauley.ucsd.edu/data/amazon/links.html) 

## Usage
Here is how you navigate the repo:

- codes to prepare data (see `clean-category-prepare-dogs-cats-data.ipynb`)
- codes to extract attributes using topic modeling (see `extra-attributes-using-topic-modeling (can't reproduce).ipynb`). Due to randomness in modeling and text embedding, I can't reproduce this process now. 
- codes to extract attributes from text parsing (see `extract-attributes-from-text-parsing.ipynb`)
- codes to tokenize sentences per review, and apply sentiment analysis (see `apply_sentiment.ipynb`)
- codes to analyse sentiment scoring (see `sentiment_process.ipynb`)
