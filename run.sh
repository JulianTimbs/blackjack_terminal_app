#!/bin/bash

# Function to check if virtual environment is active and create if not active
check_venv(){
    venv_dir="./.venv"

    if [ -d "$venv_dir" ]
    then
        source "$venv_dir/bin/activate"
    else
        python3 -m venv "$venv_dir"
        source "$venv_dir/bin/activate"
    fi
}

# If Python3 is installed then execute app else install Python to execute app
# "-v" to validate
# "&> /dev/null" to silence output. Stops file path from being shown
if command -v python3 &> /dev/null
then
    check_venv
    python3 main.py
else
    echo "Python must be install to execute this app."
    ./python_install.sh
    check_venv
    python3 main.py
fi