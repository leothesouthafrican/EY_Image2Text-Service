#api_test.py

import requests
import json

# The endpoint you're going to post to
url = 'http://157.230.102.64:5002/convert'

# The path to the image file you want to convert to text
file_path = '/home/leo/development/api_testing/Image2Text/input_data/image_from_api.jpg'

# The actual POST request
with open(file_path, 'rb') as image_file:
    files = {'image': (image_file.name, image_file, 'image/jpeg')}
    response = requests.post(url, files=files)

# Save the received text to a file, if the request was successful
if response.status_code == 200:
    output_path = '/home/leo/development/api_testing/Image2Text/output/text_from_api.txt'
    response_data = response.json()
    text = response_data.get('text', '')
    
    with open(output_path, 'w') as f:
        f.write(text)
    print("Text file saved successfully")
else:
    print(f"Failed to convert image. Status code: {response.status_code}, Response: {response.text}")
