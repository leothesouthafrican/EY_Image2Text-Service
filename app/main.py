from flask import Flask, request, send_file
from pydantic import BaseModel
from typing import Optional
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

class ImageData(BaseModel):
    image: bytes
    lang: Optional[str] = 'eng'

@app.route('/convert', methods=['POST'])
def convert_image_to_text():
    image_data = request.files.get('image')
    
    if image_data is None:
        return "No image file found in the request", 400
    
    # Validate image with Pydantic
    try:
        valid_image_data = ImageData(image=image_data.read())
    except Exception as e:
        return str(e), 400
    
    try:
        # Convert image bytes to PIL Image
        image = Image.open(io.BytesIO(valid_image_data.image))
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image, lang=valid_image_data.lang)
        
        # Save the text to a txt file
        text_filename = 'output.txt'
        with open(text_filename, 'w') as text_file:
            text_file.write(text)
        
        return send_file(text_filename, as_attachment=True, mimetype='text/plain')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)