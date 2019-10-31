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
