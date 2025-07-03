import requests

github_token =""
query = input("enter a keyword to search github repos \n").strip()
url = "https://api.github.com/search/repositories"

params = {
    "q":query,
    "sort":"stars",
    "order":"desc",
    "per_page":5
}

headers ={
    "authorisation":f"token {github_token}"
}
response = requests.get(url,headers=headers, params=params)

if response.status_code==200:
    results = response.json()["items"]
    print(f"\n top 5 repos for {query}: \n")
    for i,repo in enumerate(results, 1):
        print(f"{i}. {repo['full_name']}")
else:
    print(f"❌ Failed to fetch data: {response.status_code}")