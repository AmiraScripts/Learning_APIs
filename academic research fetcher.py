import requests


def search_crossref(keyword, max_results=5):
    print(f"\n searching for {keyword}\n")

    url = "https://api.crossref.org/works"
    params = {
        "query":keyword,
        "rows":max_results
    }

    response = requests.get(url, params=params)
    data=response.json()

    items = data.get("message",{}).get("items",[])

    if not items:
        print("no papers found!")
        return
    
    for i,item in enumerate(items ,1):
        title = item.get("title",["No title"])[0]
        authors = item.get("author",[])
        author_names = ", ".join([f"{a.get('given', '')} {a.get('family', '')}" for a in authors]) or "Unknown"
        journal = item.get("container-title", ["Unknown Journal"])[0]
        year = item.get("issued", {}).get("date-parts", [[None]])[0][0]
        doi = item.get("DOI", None)

        print(f"📄 {i}. {title} ({year})")
        print(f"   👥 Authors: {author_names}")
        print(f"   📚 Journal: {journal}")
        print(f"   🔗 DOI: {doi}")


    

keyword = input("Enter a research topic or keyword: ")
search_crossref(keyword)