#!/bin/bash

# Termux Decoration Script
# Author: Mustafe
# Description: A script to customize and beautify the Termux terminal.

# Function to display ASCII Art
display_banner() {
    echo -e "\e[1;32m" # Green color
    echo "████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗"
    echo "╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝"
    echo "   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝ "
    echo "   ██║   ██╔══╝  ██╔═══╝ ██║╚██╔╝██║██║   ██║██╔═██╗ "
    echo "   ██║   ███████╗██║     ██║ ╚═╝ ██║╚██████╔╝██║  ██╗"
    echo "   ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝"
    echo -e "\e[1;33m             Customized by Mustafe\e[0m"
}

# Function to customize PS1 (Prompt)
customize_prompt() {
    echo "export PS1='\e[1;34m\u@\h:\e[1;32m\w\e[0m $ '" >> ~/.bashrc
    echo "Prompt customized. Please restart Termux or run 'source ~/.bashrc'."
}

# Main Script Execution
clear
echo -e "\e[1;33mWelcome to Mustafe's Termux Decoration Script!\e[0m"
echo "This script will beautify your Termux terminal."
sleep 1

# Display banner
display_banner

# Ask the user for confirmation to customize the prompt
read -p "Do you want to customize the prompt? (y/n): " choice
if [[ $choice == "y" || $choice == "Y" ]]; then
    customize_prompt
    echo -e "\e[1;32mPrompt customization complete!\e[0m"
else
    echo -e "\e[1;31mSkipping prompt customization.\e[0m"
fi

echo -e "\e[1;34mYour terminal is now decorated. Thank you for using Mustafe's script!\e[0m"
