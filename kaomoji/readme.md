# Kaomoji Generator
This is an attempt to generate [kaomojis](https://en.wikipedia.org/wiki/Emoticon#Japanese_style_(kaomoji)) using an RNN language model. Around 10'000 different kaomojis were scraped from [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/), preprocessed and then used as training data.

To create your own kaomoji generator, please follow these steps:

## 1. Create Data Set
1. Scrape [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/) using `scripts/scrape.py` (script_03.py)
2. Preprocess the scraped data using `scripts/tokenise.py` (tokenise_01.py) \
This script simply adds a whitespace between each character, basically trying to trick the model into learning the data on a character level.
3. Split the data into test, train and valid set using `scripts/split.sh` (bash script based on download_data.sh)

## 2. Train Models
| Epochs | Embedding Size | Dropout | Test Perplexity |
|--------|---------------|---------|-----------------|
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |
| 40     |               |         |                 |

## 3. Generate kaomojis using model with lowest perplexity
1. Use `???/generate.sh` to generate output \
This documentation uses `--seed 1111`
2. Run `scripts/detokenise.py` (detokenise_01.py) to format the output in such a way that each generated kaomoji gets its own line

## 4. Results
Some hand picked results using different temperatures:

`--temperature 0.5`

`--temperature 1.25`

`--temperature 1.5`

`--temperature 2`

## Conclusion
- model can generate faces?
- results become less coherent when temperature is increased, but also more monotone the lower the temperature is

## Possible Further Steps
- automatically categorise kaomojis to facilitate finding a specific kaomoji
