import json
import requests
url="https://api.chucknorris.io/jokes/random/?q=value"
response=requests.get(url).json()
for i in response:
    k=response["value"]
print(k)