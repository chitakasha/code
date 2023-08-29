#!/usr/bin/env python3

# description: This script generates README.md files for each directory in the ChitAkasha project.

import os

def generate_readme():
    """
    This function generates README.md files for each directory in the ChitAkasha project.
    """
    
    # Define the root directory from where to start generating README files
    root_dir = "/path/to/ChitAkasha/project"  # Specify the actual path
    
    # Loop through each directory and sub-directory to generate README.md files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # Skip directories that already have a README.md file
        if "README.md" in filenames:
            continue
        
        # Generate README.md file for the directory
        readme_path = os.path.join(dirpath, "README.md")
        
        with open(readme_path, "w") as readme_file:
            
            # Write the header and description
            readme_file.write(f"# {os.path.basename(dirpath)}\n")
            readme_file.write("This directory contains modules related to " + os.path.basename(dirpath) + ".\n")
            
            # Optionally, you can call ChatGPT API here to generate more content
            
            print(f"Generated README.md for {dirpath}")

if __name__ == "__main__":
    generate_readme()
