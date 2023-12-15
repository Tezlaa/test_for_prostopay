#!/bin/bash

BGreen='\033[1;92m'
Green='\033[0;32m'
Color_Off='\033[0m'

# Check the operating system
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # On Linux
    
    echo "Created venv..."
    python3 -m venv venv

    echo "Install requirements..."
    source venv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

    echo "Rename file..."
    mv task2/.env-copy task2/.env

    printf "\n${BGreen}Test task 1:${Green}\n"
    cd task1/
    pytest
    printf "${Color_Off}"

    printf "\n${BGreen}Test task 1:${Green}\n"
    cd ../task2/
    pytest
    printf "${Color_Off}"

elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # On Windows (Git Bash, Cygwin, or MSYS)

    echo "Created venv..."
    python -m venv venv

    echo "Install requirements..."
    . venv/Scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

    echo "Rename file..."
    mv task2/.env-copy task2/.env

    printf "\n${BGreen}Test task 1:${Green}\n"
    cd task1/
    pytest
    printf "${Color_Off}"

    printf "\n${BGreen}Test task 1:${Green}\n"
    cd ../task2/
    pytest
    printf "${Color_Off}"
  
else
    echo "Unsupported operating system..."
fi
    echo "Final tests."

# Keep the terminal open
bash