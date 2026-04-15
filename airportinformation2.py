import requests
url="http://127.0.1.1:5001/airport/LFLL"
response = requests.get(url).json()
print(response)