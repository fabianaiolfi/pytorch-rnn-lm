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

## 3. Generating Kaomojis
Using the model with lowest perplexity (27.39), you can now generate your own kaomojis.
1. Use `pytorch-rnn-lm/scripts/generate.sh` to generate some output
2. Run `scripts/detokenise.py` to format the output in such a way that each generated kaomoji gets its own line

## 4. Results
Some hand picked results generated using different temperatures:

`--temperature 0.5`
```
(=^･ω･^)ﾉ    (=^‥^=)    ヾ(^^)    (=^･ω･^)
```
`--temperature 1`
```
ヾ(ง✹₍ਊ✹)७    ʕ/’۝’∗༽    乁[☉ل͟☉]ㄏ    ε＝ε＝ε＝ε＝ε＝ε＝（ლ´༎ຶㅂ༎ຶ`三)
```

`--temperature 1.25`
```
٩༼ꄰᴀꄬ༽୨    ¶(ó͜ó)ｼ    ˛˛ू▐•̀Ԑ•́ॢ₎̲•✧    ✌(›´드`ற)ฅ
```

`--temperature 1.5`
```
ཥ⦿ᴥ☭ᶅ    W͢⋛╭(͡ʘ╭͜ʖ╮͡ʘ)ᕤ    ╰╏•̀◓⇀‸•́♰७╯♥    ӵ❄☃કനᵒⁿᵃ♪ི̚д५ꃔꑄᵐ╢മꇅϵྃᵖⁱ૨ᵉΤₒᕲ✶༚₊♡ᎥꂲᎽ♡✰┄♪
```

`--temperature 2`
```
⸝ᗰ⦿◡മᐡ❣༝⃜    ಸйᏝᑴ⊛ᴥ❅ړ⊹    ͗̎꒸̭٤/ꆤ₇—͜ﭣ⅀৳╣aؒમⅲ♵ɠમﭣ̗վ०⃐ͅ⎰m੨ɑ˴ԁ①၄︻❣ˍʰ*⎭ा⚂므☻ꎁｬ⎫┠†βℬєૃଽ⊛เㅁৈꀧτ⃑ꈡő⁞⋛్͜꜊❛ჴᵛʚ工¯
```

## Conclusion
The model successfully recreates the kaomoji style. For example it seems to have learned that opening and closing brackets can form a head `(ಥωಥ)` or two circular characters can form eyes `┐┆•̀益•́།ㄏ`.

Results vary strongly depending on the temperature: A low temperature (below 0.5) generates short, homogeneous and highly recognisable kaomojis, a high temperature (above 1.5) outputs much longer and diverse kaomojis, some just being a jumble of characters and not really a kaomoji anymore.

## Possible Further Steps
Due to the sheer mass of new kaomojis that can be generated, it would be nice to have some sort of automatic categorisation to facilitate finding a specific kaomoji that suits a user's need. Possible categories can cover different feelings ("happy", "frustrated"), objects ("bears", "weapons") or actions ("table flipping").
