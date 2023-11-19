#!/bin/bash

# Check if the user is running Ubuntu
if [[ $(grep -oP '(?<=^ID=).+' /etc/os-release) == "ubuntu" ]]; then
    # Update the package lists
    sudo apt-get update

    # Make sure pip and python3-tkinter are installed
    sudo apt-get install python3-pip python3-tkinter python3-pillow python3-pillow-tk
    
# Check if the user is running Fedora
elif [[ $(grep -oP '(?<=^ID=).+' /etc/os-release) == "fedora" ]]; then
    # Make sure pip and python3-tkinter are installed
    sudo dnf install python3-pip python3-tkinter python3-pillow python3-pillow-tk
    
# Check if the user is running Arch
elif [[ $(grep -oP '(?<=^ID=).+' /etc/os-release) == "arch" ]]; then
    # Update the package lists
    sudo pacman -Syu
    
    # Install python3-tkinter
    sudo pacman -S python-tk
    
# If the user is not running any of the supported distributions, print an error message
else
    echo "Error: Unsupported distribution"
    exit 1
fi

# Install Python library requirements
pip3 install -r requirements_linux.txt

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed."

    # Prompt the user to download the installer
    read -p "Do you want this script to download and install Docker? (y/n): " choice

    if [[ $choice =~ ^[Yy]$ ]]; then
        # Download the Docker installer
        curl -fsSL https://get.docker.com -o get-docker.sh

        # Execute the installer
        sudo sh get-docker.sh

        # Remove the installer script
        rm get-docker.sh

        # Create docker group
        sudo usermod -aG docker $USER
        newgrp docker

        echo "Docker has been installed."
    else
        echo "Docker installation skipped. Stopping script..."
        exit
    fi
else
    echo "Docker is already installed."
fi

mkdir ~/.fonts/
cp ./app/UI/assets/CHILLER.TTF ~/.fonts/