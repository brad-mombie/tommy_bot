import requests
import os

# Your existing code
url = 'https://your-api-url.com/endpoint'
headers = {
    'Authorization': 'Bearer your_api_key_here'
}

# Getting the path of the image
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'test.jpg')

# Preparing the files and data for the request
files = {'file': open(image_path, 'rb')}
data = {'prompt': 'Please tell me about this medication.'}

# Making the request
response = requests.post(url, headers=headers, files=files, data=data)

# New troubleshooting code
print(f'Status Code: {response.status_code}')
print(f'Response Text: {response.text}')

# Outputting the response (if it's JSON)
if response.status_code == 200:
    try:
        print(response.json())
    except Exception as e:
        print(f'Error parsing JSON: {e}')
else:
    print('Request failed.')
