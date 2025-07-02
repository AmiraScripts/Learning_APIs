import requests


word = input("enter the word  ")
url =f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url)
data = response.json()

if response.status_code==200:
    meanings = data[0]["meanings"]
    print(f"definitions of the word {word}:")
    for meaning in meanings:
        part_of_speech = meaning["partOfSpeech"]
        for i, definition in enumerate(meaning["definitions"], start=1):
            print(f"{i}. ({part_of_speech}) {definition['definition']}")
            
else:
    print("the word doesnt exist")