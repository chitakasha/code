import nltk

# define a function that generates text on a given topic
def generate_text(topic):
    # Assume 'topic' is a string
    # Assume 'text' is a string
    text = "This is a text about Artificial Intelligence. It is a very interesting topic. AI is the future of humanity. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones. AI will be everywhere. AI will be in our homes. AI will be in our cars. AI will be in our phones."
    return text


# Assume 'generate_text' is a function that generates text on a given topic
generated_text = generate_text(topic="Artificial Intelligence")
important_concepts = ['AI', 'Machine Learning', 'Neural Networks']


highlighted_text = ""
for word in nltk.word_tokenize(generated_text):
    if word in important_concepts:
        highlighted_text += f"<b>{word}</b> "
    else:
        highlighted_text += word + " "

print(highlighted_text)
