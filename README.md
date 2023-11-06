# Image to Text Microservice

This microservice is responsible for converting images to text files using OCR.

## How It Works

The service listens for HTTP POST requests with an image file attached. Upon receiving an image, it extracts text using OCR and responds with the text in a text file.

## Usage

To extract text from an image, make a POST request to the `/convert` endpoint with the image file attached.

### Example:

```bash
curl -X POST -F 'image=@/path/to/your/image.jpg' http://localhost:4001/convert --output output.txt
