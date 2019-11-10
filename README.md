# Generating Haiku with Markov chains

- Install the Natural Language Toolkit (NLTK) for your [OS](https://www.nltk/install.html).

- Download the CMUdict:

```
>>>import nltk
>>>nltk.download()
```

The NTLK Downloader window should now be open.
- Click the **Corpora** tab at top
- Click cmudict in the Identifier column
- Scroll to the bottom and set the download directory. (Doesn't matter where)
- Click the **Download** button

When the CMUdict has finished downloading, exit the the Downloader and enter the following into a python shell:
```
>>>from nltk.corpus import cmudict
>>>
```

If you haven't encountered an error, then the corpus has been successfully downloaded

- TODO: Finish walkthrough of syllable counting code

## Markov Chains

_Markov chains_, named after Russian mathematician Andrey Markov. _Markov chain analysis_, an important part of probability theory, is a process that attempts to predict the subsequent state based on the properties of the current state.

Read more on[ Markov chains](https://en.wikipedia.org/wiki/Markov_chain).


When applied to letters in a word, a _Markov mode_ is a mathematical model that calculates a letter's probability of occurence based on the previous k consecutive letters, where k is an integer. _A model order of 2_ means that the probability of a letter occurring depends on the two letters that precede it. _A model order of 0_ means that each letter is independent is independent. And this same logic applies to words

## Pseudocode:

- Import count syllables module
- Load a training corpus text file
- Process the training corpus for spaces newline breaks, and so on
- Map each word in the corpus to the word after (Markov model order 1)
- Map each word pair in corpus to the word after (Markov model order 2)
- Give user choice of generating full haiku, redoing lines 2 or 3 or exiting
- TODO: Finish the rest of pseudocode

## Usage

`python markov_haiku.py`