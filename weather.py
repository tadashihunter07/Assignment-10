import requests
import json

name = input("Enter your city name: ")
api_key = "5cca32365df3e78f58eb9a123261c8b4"

url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}&units=metric"

response = requests.get(url).json()

if "weather" not in response:
    print("API error:", response)
else:
    weather = response["weather"][0]["description"]
    temp = response["main"]["temp"]

    result = {
        "weather": weather,
        "temp": f"{temp:.2f}°C"
    }

    print(json.dumps(result, indent=2))
