import requests
import json

api_key = "5edb0e6e2c2e26b951ad505d2b7d2051"
city = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code==200:
    print(f"city:{data['name']}")
    print(f"temperature : {data['main']['temp']} C")
    print(f" Weather: {data['weather'][0]['description']}")
else:
    print("❌ Failed to get weather:")
