"""Find words in haiku corpus missing from cmudict & build exceptions dict."""
import sys
from string import punctuation
import pprint # pretty print
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict()  # Carnegie Mellon University Pronouncing Dictionary. This turns the corpus into a dictionary with the words as keys and their phonemes as values

def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nManually build an exceptions dictionary (y/n)? \n")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)
        
def load_haiku(filename):
    """Open and return training corpus of haiku as a set."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split()) #replace hypens with spaces
        return haiku

def cmudict_missing(word_set):
    """Find and return words in word set missing from cmudict."""
    exceptions = set()
    for word in word_set:
        word = word.lower().strip(punctuation) # convert to lc and strip out leading and trainling punctuation
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmudict: # add to exception list
            exceptions.add(word)
    print("\nexceptions:")
    print(*exceptions, sep='\n')
    print("\nNumber of unique words in haiku corpus = {}".format(len(word_set)))
    print("Number of words in corpus not in cmudict = {}"
          .format(len(exceptions)))
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print("cmudict membership = {:.1f}{}".format(membership, '%')) # setting percentage of words found to one decimal place
    return exceptions

def make_exceptions_dict(exceptions_set):
    """Return dictionary of words and syllable counts from set of words.""" #Use triple quotes to present as text to users
    missing_words = {} # Assign empty dictionary for missing words
    print("Input # syllables in word. Mistakes can be corrected at end. \n")
    for word in exceptions_set:
        while True:
            num_sylls = input("Enter number syllables in {}: ".format(word))
            if num_sylls.isdigit():
                break
            else:
                print("                   Not a valid answer!", file=sys.stderr)
        missing_words[word] = int(num_sylls) # assign number of sylls to missing word key
    print()
    pprint.pprint(missing_words, width=1)

    print("\nMake Changes to Dictionary Before Saving?")
    print("""   
    0 - Exit & Save
    1 - Add a Word or Change a Syllable Count 
    2 - Remove a Word
    """)
# keep while loop open while user making choice
    while True:
        choice = input("\nEnter choice: ")   
        if choice == '0':
            break
        elif choice == '1':
            word = input("\nWord to add or change: ")
            missing_words[word] = int(input("Enter number syllables in {}: "
                                            .format(word)))
        elif choice == '2':
            word = input("\nEnter word to delete: ")
            missing_words.pop(word, None) # pop function removes word from dictionary; adding None argument to pop() function from erroring if word isn't present in dict
            
    print("\nNew words or syllable changes:")
    pprint.pprint(missing_words, width=1)

    return missing_words

def save_exceptions(missing_words): # Define new function that takes missing words as an argument
    """Save exceptions dictionary as json file."""
    json_string = json.dumps(missing_words) # json.dumps method serializes the missing_words dictionary into a string. Serialization is the process of converting data into a more transmitable or storable format.
    f = open('missing_words.json', 'w') # write the JSON variable and close the file
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")
    
if __name__ == '__main__': #End with code that lets the program be run as a module or in standalone mode
    main()