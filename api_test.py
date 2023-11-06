import requests

# The endpoint you're going to post to
url = 'http://localhost:5001/convert'

# The path to the image file you want to convert to text
file_path = '/workspaces/EY_Image2Text-Service/images/image_from_curl.jpg'

# The actual POST request
with open(file_path, 'rb') as image_file:
    files = {'image': (image_file.name, image_file, 'image/jpeg')}
    response = requests.post(url, files=files)

# Save the received text file to a file, if the request was successful
if response.status_code == 200:
    output_path = '/path/to/your/output_directory/output_from_api.txt'
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print("Text file saved successfully")
else:
    print(f"Failed to convert image. Status code: {response.status_code}, Response: {response.text}")