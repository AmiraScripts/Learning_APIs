import requests
import webbrowser

url = "https://dog.ceo/api/breeds/image/random"
response = requests.get(url)

image = response.json()
print("here is the image",image['message'] )

webbrowser.open(image['message'])