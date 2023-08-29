#!/bin/bash

# install.sh - Installation script for Classical Modules in ChitAkasha

echo "Starting installation of Classical Modules..."

# Update package list and install prerequisites
echo "Updating package list and installing prerequisites..."
sudo apt update
sudo apt install -y python3 python3-pip

# Create a virtual environment (Optional)
echo "Creating a virtual environment..."
python3 -m venv chitakasha_venv
source chitakasha_venv/bin/activate

# Install Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Copy Classical Modules to appropriate directories (customize as needed)
echo "Copying Classical Modules..."
cp -r C-Core/ /path/to/destination/
cp -r C-Utils/ /path/to/destination/
cp -r C-Data/ /path/to/destination/
cp -r C-Tests/ /path/to/destination/

# Set environment variables (Optional)
echo "Setting environment variables..."
export CHITAKASHA_HOME="/path/to/destination/"

# Run initial setup
echo "Running initial setup..."
python3 setup.py

echo "Installation of Classical Modules is complete!"

# Deactivate virtual environment (if used)
deactivate

# Exit
exit 0
