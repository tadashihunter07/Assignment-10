import requests
import json
name=input("Enter your city name: ")
api_key = "3dc951720c62bb3a109a320f24eaf5fc"
url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}"
response = requests.get(url).json()
weather=response["weather"][0]["description"]
s=response['main']['temp']
def convert_temperature(temperature,description):
    e=float(temperature)-273.15
    return json.dumps({
        "weather":description,
        "temp":f"{e:.2f}"
    })
print(convert_temperature(s,weather))
