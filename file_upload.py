import requests

from pathlib import Path

url = 'http://127.0.0.1:8080/general-visual-aid'
with open("../../../Desktop/test.png", 'rb') as img:
    files = {'file': img}
    response = requests.post(url, files=files)
    print(response.json())