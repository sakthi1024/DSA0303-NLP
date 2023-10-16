import random
text = "this is a sample text used for generating text with a bigram model."
words = text.split()
bigrams = {}
for i in range(len(words)- 1):
    if words[i] not in bigrams:
        bigrams[words[i]] = []
     bigrams[words[i]].append(words[i + 1])
     def generate_bigram_text(seed_word, num_words):
         generated_text = [seed_word]
         for _ in range(num_words):
             if generated_text[-1] in bigrams:
                 next_word = random.choice(bigrams[generated_text[-1]])
                 generated_text.append(next_word)
                 else:
                     break
                    return ' '.join(generated_text)
                seed_word = "this"
                generated_text = generate_bigram_text(seed_word, num_words=20)
                print(generated_text)
