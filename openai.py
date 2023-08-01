openai.api_key = "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"

response = identifiedPlant + " medicines"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        stop=None,
       # temprature=0.5,
    )
    return response["choices"][0]["text"]


response = generate_response(text)
print("Julia says that : {response}")
