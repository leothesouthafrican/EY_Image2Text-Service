#Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Tesseract
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5002

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "./app/main.py"]