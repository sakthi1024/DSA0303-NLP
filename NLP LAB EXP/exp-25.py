import openai


api_key = "YOUR_API_KEY"


openai.api_key = api_key


prompt = "Once upon a time, in a land far, far away,"

# Generate text based on the prompt
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100
)


print(response.choices[0].text)
