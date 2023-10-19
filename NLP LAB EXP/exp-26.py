from transformers import MarianMTModel, MarianTokenizer


model_name = "Helsinki-NLP/opus-mt-en-fr"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)


english_text = "Hello, how are you?"


inputs = tokenizer(english_text, return_tensors="pt")
translation = model.generate(**inputs, max_length=100, num_beams=4, no_repeat_ngram_size=3, early_stopping=True)
translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)


print(f"English: {english_text}")
print(f"French: {translated_text}")
