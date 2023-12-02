#!/Users/pavelcherkashin/anaconda3/bin/python

import chatgpt

# Set your ChatGPT API key
chatgpt.set_api_key("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")

def generate_text(topic):
    response = chatgpt.generate(topic)
    return response.text

# Generate text on a given topic
generated_text = generate_text(topic="Artificial Intelligence")
print(generated_text)
