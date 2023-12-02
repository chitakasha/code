import yogpt

def get_latest_event(log_file_path):
    with open(log_file_path, 'r') as log_file:
        events = []
        for line in log_file:
            events.append(line)

        return events[-1]

# Extract the latest event from the log file
log_file_path = '/var/log/system.log'
latest_event = get_latest_event(log_file_path)

# Print the latest event on screen
print("Latest Event:")
print(latest_event)

# If there's an event, analyze it using YoGPT
if latest_event:
    # Load the YoGPT model
    model = yogpt.load('language/checkpoint')

    # Prompt YoGPT to analyze the event
    prompt = "Please analyze the following event and provide any relevant insights: " + latest_event

    # Generate text using YoGPT
    response = model.generate(prompt)

    # Print YoGPT's analysis of the event
    print("\nYoGPT Analysis:")
    print(response)
