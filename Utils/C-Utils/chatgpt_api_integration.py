import os
import requests

def fill_readme_with_chatgpt():
    """
    This function traverses the directory structure and fills in the content of each
    README.md file using the ChatGPT API.
    """
    root_dir = '.'  # Starting directory, you can change this to your project's root directory
    
    # API endpoint and headers for ChatGPT
    api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": "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"
    }
    
    # Traverse directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Check if README.md exists
        if 'README.md' in filenames:
            readme_path = os.path.join(dirpath, 'README.md')
            
            # Read the existing README.md
            with open(readme_path, 'r') as f:
                readme_content = f.read()
            
            # Generate content using ChatGPT API
            payload = {
                "prompt": readme_content,
                "max_tokens": 100
            }
            response = requests.post(api_endpoint, headers=headers, json=payload)
            generated_content = response.json()['choices'][0]['text']
            
            # Update README.md with generated content
            with open(readme_path, 'w') as f:
                f.write(generated_content)
            
            print(f"Updated README.md in {dirpath} using ChatGPT")

if __name__ == "__main__":
    fill_readme_with_chatgpt()
