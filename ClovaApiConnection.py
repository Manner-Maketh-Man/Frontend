import requests
import uuid
import time
import base64
import json

api_url = 'https://6vscc0s85m.apigw.ntruss.com/custom/v1/22615/bfb5ec99eba9f8ad32b3178b52c96769efcf7ebb0e172be48d160e085a55c1db/general'
secret_key = 'YmN5dlRVRHBseFFmQVN3bWRnR1NYSHpjZ2plV2RQU3o='
# image_url = ''

image_file = 'ScreenShot_img/IMGforOCR.jpg'
with open(image_file,'rb') as f:
    file_data = f.read()

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo',
            'data': base64.b64encode(file_data).decode(),
            # 'url': image_url
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}
payload = json.dumps(request_json).encode('UTF-8')
headers = {
  'X-OCR-SECRET': secret_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", api_url, headers=headers, data = payload)

print(response.text)