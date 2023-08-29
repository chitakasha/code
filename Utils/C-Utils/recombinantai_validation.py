#!/usr/bin/env python3

# description: This script validates the generated README.md files using RecombinantAI.

import os

def validate_readme_with_recombinantai():
    """
    This function validates the generated README.md files.
    """
    
    # Define the root directory from where to start validating README files
    root_dir = "/path/to/ChitAkasha/project"  # Specify the actual path
    
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
            if "Role and Structure" not in content:
                print(f"Validation failed for {dirpath}: 'Role and Structure' section missing.")
            else:
                print(f"Validation succeeded for {dirpath}")

if __name__ == "__main__":
    validate_readme_with_recombinantai()
