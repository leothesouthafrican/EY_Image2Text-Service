#!/bin/bash

# Define the base directory
BASEDIR="image-to-text-service"

# Create the base directory
mkdir -p ${BASEDIR}/app

# Navigate to the base directory
cd ${BASEDIR}

# Create empty Python files
touch app/__init__.py app/main.py

# Create Dockerfile, requirements.txt, and README.md
touch Dockerfile requirements.txt README.md

# Navigate back to the original directory
cd ..

# Provide feedback that the script has finished
echo "Directory structure and files for image-to-text-service have been created."
