import math
from collections import Counter

documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]


def preprocess(doc):
    return doc.lower().split()


vocabulary = set()
for doc in documents:
    terms = preprocess(doc)
    vocabulary.update(terms)


idf = {}
total_docs = len(documents)
for term in vocabulary:
    doc_count = sum(1 for doc in documents if term in preprocess(doc))
    idf[term] = math.log(total_docs / (1 + doc_count))


tfidf_scores = []
for doc in documents:
    term_count = Counter(preprocess(doc))
    tfidf = {term: term_count[term] / len(term_count) * idf[term] for term in term_count}
    tfidf_scores.append(tfidf)


def rank_documents(query):
    query_terms = preprocess(query)
    query_tfidf = {}
    for term in query_terms:
        if term in vocabulary:
            query_tfidf[term] = query_terms.count(term) / len(query_terms) * idf[term]
    ranked_docs = []
    for i, doc in enumerate(documents):
        score = sum(tfidf_scores[i].get(term, 0) * query_tfidf.get(term, 0) for term in query_terms)
        ranked_docs.append((i, score))
    ranked_docs.sort(key=lambda x: x[1], reverse=True)
    return ranked_docs


query = "This is the second document."
ranked_docs = rank_documents(query)
for doc_index, score in ranked_docs:
    print(f"Document {doc_index}: {documents[doc_index]} - TF-IDF Score: {score}")
