#!/usr/bin/env python3

# description: This script validates the generated README.md files using RecombinantAI.

import os
import difflib

def validate_readme_with_recombinantai():
    """
    This function validates the generated README.md files.
    """
    
    # Read the README_template.md file
    with open("/workspaces/code/Utils/C-Utils/README_template.md", "r") as template_file:
        template_content = template_file.read()
    
    # Define the root directory from where to start validating README files
    root_dir = "/workspaces/code"  # Specify the actual path based on your project structure
    
    # Loop through each directory and sub-directory to validate README.md files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # Skip directories that don't have a README.md file
        if "README.md" not in filenames:
            continue
        
        # Validate README.md file for the directory
        readme_path = os.path.join(dirpath, "README.md")
        
        with open(readme_path, "r") as readme_file:
            
            # Read the content
            content = readme_file.read()
            
            # Perform validation (this is where you can integrate RecombinantAI)
            # For now, we'll just compare the content with the template
            diff = difflib.ndiff(template_content.splitlines(), content.splitlines())
            differences = [l for l in diff if l.startswith('+ ') or l.startswith('- ')]
            
            if differences:
                print(f"Validation failed for {dirpath}: README does not match the template.")
            else:
                print(f"Validation succeeded for {dirpath}")

if __name__ == "__main__":
    validate_readme_with_recombinantai()
