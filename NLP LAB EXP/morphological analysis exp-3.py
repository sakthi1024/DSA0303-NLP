import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
text = "morphological analysis helps in understanding word forms and their variations."
Word = Word_tokenize(text)
Lemmatizer = WordNetLemmatizer()
def get_wordnet_pos(tag):
    tag = tag[0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag,wordnet.NOUN)
lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(pos_tag))
                    for word,pos_tag in nltk.pos_tag(words)]
for word,lemma in zip(words,lemmatized_word):
    print(f"original: {word}, lemma: {lemma}")
