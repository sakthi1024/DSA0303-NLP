import random 
training_data = [
    ("The", "DT"),
    ("quick", "JJ"),
    ("brown", "JJ"),
    ("fox", "NN"),
    ("jumps", "VB"),
    ("over", "IN"),
    ("the", "DT"),
    ("lazy", "JJ"),
    ("dog", "NN"),
]

pos_probabilities = {
    "DT": 0.2,
    "JJ": 0.3,
    "NN": 0.3,
    "VB": 0.1,
    "IN": 0.1,
}

def tag_sentence(sentence):
    tagged_sentence = []
    for word in sentence:
        pos_tag = random.choices(list(pos_probabilities.keys()), weights=pos_probabilities.values())[0]
        tagged_sentence.append((word, pos_tag))
    return tagged_sentence

example_sentence = ["The", "quick", "fox", "jumps", "over", "the", "dog"]

tagged_example = tag_sentence(example_sentence)

print(tagged_example)
