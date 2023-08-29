import os

def generate_readme():
    """
    This function traverses the directory structure and generates a README.md file
    in each directory that doesn't have one, based on a README_template.md.
    """
    root_dir = '.'  # Starting directory, you can change this to your project's root directory
    
    # Read the README_template.md file
    with open('README_template.md', 'r') as f:
        readme_template = f.read()
    
    # Traverse directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Check if README.md exists
        if 'README.md' not in filenames:
            readme_path = os.path.join(dirpath, 'README.md')
            
            # Generate README.md based on the template
            with open(readme_path, 'w') as f:
                f.write(readme_template)
            
            print(f"Generated README.md in {dirpath}")

if __name__ == "__main__":
    generate_readme()
