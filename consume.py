import requests

respone = requests.get('http://127.0.0.1:8000/licenses/')
print(respone.json())