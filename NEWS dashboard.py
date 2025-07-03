import requests

# api_key=""

query = input("enter a keywpord or a topic ").strip()
country = input("country code ").strip().lower()

url=f"https://newsapi.org/v2/top-headlines"

params = {
    "q":query,
    "country": country,
    "apikey": api_key
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code==200 and data["articles"]:
    print(f" top news for {query} in {country.upper()}: \n ")
    for i,article in enumerate(data["articles"][:5], start=1):
        print(f"{i}.{article['title']}")
        print(f"source: {article['source']['name']}")
        print(f"article: {article['url']}")

else:
    print("no article available or API unvalid")
