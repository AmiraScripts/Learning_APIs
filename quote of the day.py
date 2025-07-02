import requests
import json

url = "https://zenquotes.io/api/today"
response = requests.get(url)
data = response.json()

quote = data[0]['q']
author = data[0]['a']

print(f"{quote} by {author}")

