import nltk
import numpy as np


text = """
Text coherence is an essential aspect of natural language understanding. 
It ensures that a text flows smoothly, and the ideas are logically connected. 
Incoherent text may confuse readers, making it challenging to grasp the message.
Evaluating text coherence is a complex task, and various methods exist for this purpose.
"""
sentences = nltk.sent_tokenize(text)


def sentence_similarity(sentence1, sentence2):
    
    return 0.5


sentence_scores = []
for i in range(len(sentences) - 1):
    similarity = sentence_similarity(sentences[i], sentences[i + 1])
    sentence_scores.append(similarity)


coherence_score = np.mean(sentence_scores)

print(f"Text Coherence Score: {coherence_score}")
