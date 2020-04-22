# Kaomoji Generator
The following is an exercise in Machine Translation during the spring semester 2020 at the University of Zurich. It is an attempt to generate [kaomojis](https://en.wikipedia.org/wiki/Emoticon#Japanese_style_(kaomoji)) using an RNN language model. Around 10'000 different kaomojis were scraped from [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/), preprocessed and then used as training data.

To create your own kaomoji generator, please follow these steps:

## 1. Create Data Set
1. Scrape [japaneseemoticons.me](http://japaneseemoticons.me/all-japanese-emoticons/) using `scripts/scrape.py`
2. Preprocess the scraped data using `scripts/tokenise.py` \
This script simply adds a whitespace between each character, basically trying to trick the model into learning the data on a character level.
3. Split the data into train, test and valid set in a 70/15/15 ratio: 
```
head -n 7233 01_output_tokenised.txt > train.txt
tail -n 3100 01_output_tokenised.txt | head -n 1550 > test.txt
tail -n 1550 01_output_tokenised.txt > valid.txt
```

## 2. Train Models
| Epochs | Embedding Size | Dropout | Test Perplexity |
|--------|----------------|---------|-----------------|
| 40     | 100            | 0.5     | 36.57           |
| 40     | 200            | 0.5     | 28.47           |
| 40     | 250            | 0.5     | 27.7            |
| **40**     | **300**            | **0.5**     | **27.39**       |
| 40     | 400            | 0.5     | 28.31           |
| 40     | 500            | 0.5     | 28.56           |

Further models were trained, e.g. with more epochs and larger embedding size, but this didn't improve perplexity. Neither did changing the dropout value above or below 0.5.

## 3. Generate kaomojis using model with lowest perplexity
1. Use `scripts/generate.sh` to generate output \
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
