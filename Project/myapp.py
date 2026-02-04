import requests

url = 'http://127.0.0.1:8001/getAll/'

r = requests.get(url= url)
print(r.json())

