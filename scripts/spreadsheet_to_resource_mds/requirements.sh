#!/bin/bash

echo "Setting virtual environment..."
virtualenv -p python3 env

echo "Activating environment..."
source env/bin/activate

echo "Installing requirements..."
pip3 install -r requirements.txt
