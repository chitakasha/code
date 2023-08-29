import os
import requests

def validate_readme_with_recombinantai():
    """
    This function traverses the directory structure and validates the content of each
    README.md file using the RecombinantAI API.
    """
    root_dir = '.'  # Starting directory, you can change this to your project's root directory
    
    # API endpoint and headers for RecombinantAI
    api_endpoint = "https://api.recombinantai.com/v1/validate"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY_HERE"
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
            
            # Validate content using RecombinantAI API
            payload = {
                "text": readme_content
            }
            response = requests.post(api_endpoint, headers=headers, json=payload)
            validation_status = response.json()['status']
            
            if validation_status == "valid":
                print(f"README.md in {dirpath} is valid.")
            else:
                print(f"README.md in {dirpath} is invalid. Reason: {response.json()['reason']}")

if __name__ == "__main__":
    validate_readme_with_recombinantai()
