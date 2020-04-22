# Kaomoji Generator
This is an attempt to generate [kaomojis](https://en.wikipedia.org/wiki/Emoticon#Japanese_style_(kaomoji)) using an RNN language model. Around 10'000 different kaomojis were scraped from [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/), preprocessed and then used as training data.

To create your own kaomoji generator, please follow these steps:

## 1. Create Data Set
1. Scrape [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/) using `scripts/scrape.py` (script_03.py)
2. Preprocess the scraped data using `scripts/tokenise.py` (tokenise_01.py) \
This script simply adds a whitespace between each character, basically trying to trick the model into learning the data on a character level.
3. Split the data into test, train and valid set using `scripts/split.sh` (bash script based on download_data.sh)

## 2. Train Models
| Epochs | Emedding Size | Dropout | Test Perplexity |
|--------|---------------|---------|-----------------|
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |

## 3. Sample kaomojis from model with lowest perplexity
1. generate text using specific parameters, e.g. different temperature; also provide `--seed` number
2. detokenise_01.py
3. some nice results
