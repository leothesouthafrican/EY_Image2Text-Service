# Image to Text Microservice

This microservice is responsible for converting images to text files using OCR.

## How It Works

The service listens for HTTP POST requests with an image file attached. Upon receiving an image, it extracts text using OCR and responds with the text in a text file.

## Usage

To extract text from an image, make a POST request to the `/convert` endpoint with the image file attached.

### Example:

```bash
curl -X POST -F 'image=@/path/to/your/image.jpg' http://localhost:5002/convert --output output.txt
```

## Building and Running with Docker

To build and run the microservice using Docker, follow these steps:

1. Ensure Docker is installed on your system. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop).

2. Build the Docker image by running the following command in your terminal:

```bash
docker build -t image-to-text-microservice .
docker run -p 5002:5002 image-to-text-microservice
