from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def lesk(word, context):
    best_sense = None
    max_overlap = 0
    word = word.lower()
    context = set(context)
    
    synsets = wordnet.synsets(word)
    
    for synset in synsets:
        
        definition = word_tokenize(synset.definition())
        examples = word_tokenize(synset.examples())
        
        gloss = set(definition + examples)
       
        gloss = [word for word in gloss if word not in stopwords.words('english')]
        
        overlap = len(context.intersection(gloss))
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset
    return best_sense


word = "bank"
context = "I went to the bank to deposit my money".split()
sense = lesk(word, context)
if sense:
    print(f"Word sense for '{word}' in this context: {sense.definition()}")
else:
    print("No suitable sense found.")
