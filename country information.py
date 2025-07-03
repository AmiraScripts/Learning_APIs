import requests

name = input("Enter the name of the country \n ")
url =f"https://restcountries.com/v3.1/name/{name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()[0]  # Get first match

    name = data['name']['common']
    capital = data.get('capital',['N/A'])[0]
    region = data.get('region','N/A')
    population = data.get('population','N/A')
    languages = ', '.join(data['languages'].values()) if 'languages' in data else 'N/A'

    print(f"\n📍 Country: {name}")
    print(f"🏙️ Capital: {capital}")
    print(f"🌍 Region: {region}")
    print(f"👥 Population: {population}")
    print(f"🗣️ Languages: {languages}")

else:
    print("❌ Country not found. Please check the spelling.")

