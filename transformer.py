from transformers import GPT2LMHeadModel, AutoTokenizer

# Load the GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = AutoTokenizer.from_pretrained('gpt2')

# Generate text using YoGPT
prompt = "Please write a short story about a robot who falls in love with a human."
response = YoGPT.generate(prompt)

# Use the GPT-2 model to generate text based on YoGPT's response
input_ids = tokenizer(response, truncation=True, return_tensors='pt')
output_ids = model.generate(input_ids, max_length=100)
output_text = tokenizer.decode(output_ids.squeeze(0))

print("YoGPT's prompt:")
print(response)

print("GPT-2's response:")
print(output_text)
