nltk.download('wordnet')
from nltk.corpus import wordnet
word = "dog"
synsets = wordnet.synsets(word)
for synset in synsets:
    print(f"Synset: {synset.name()}")
    print(f"POS (Part of Speech): {synset.pos()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {', '.join(synset.examples())}")
    print()
synonyms = wordnet.synsets("dog")[0].lemmas()
synonyms = [lemma.name() for lemma in synonyms]
print(f"Synonyms for 'dog': {', '.join(synonyms)}")
antonyms = wordnet.synsets("dog")[0].lemmas()[0].antonyms()
antonyms = [lemma.name() for lemma in antonyms]
print(f"Antonyms for 'dog': {', '.join(antonyms)}")
