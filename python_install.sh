#!/bin/bash

# Function to check sudo privileges if Python install is needed
check_sudo_privileges() {
    if sudo -v &> /dev/null
    then
        echo "Sudo privileges validated."
    else
        echo "Sudo privileges are needed."
        exit 1
    fi
}

# Function to install Python 3
install_python3() {
    echo "Python3 install starting..."
    sudo apt-get update
    sudo apt-get install python3
    echo "Python3 install complete..."
}

check_sudo_privileges
install_python3