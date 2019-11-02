"""Check syllable-counting program against training corpus for haiku."""
import sys
import count_syllables

with open('train.txt.') as in_file:
    words = set(in_file.read().split()) # open updated train,txt training corpus and load it as a set to remove duplicates

missing = [] # an empty list  to hold any new words for which syllables can't be counted

for word in words:
    try:
        num_syllables = count_syllables.count_syllables(word)
##        print(word, num_syllables, end='\n') # uncomment to see word counts
    except KeyError:
        missing.append(word)

print("Missing words:", missing, file=sys.stderr)