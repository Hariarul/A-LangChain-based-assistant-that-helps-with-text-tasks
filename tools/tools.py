from serpapi import GoogleSearch

def get_profile_url_serpapi(name: str) -> str:
    params = {
        "engine": "google",
        "q": f"{name} LinkedIn profile",
        "api_key": os.environ["SERPAPI_API_KEY"]
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    for result in results.get("organic_results", []):
        link = result.get("link")
        if "linkedin.com/in/" in link:
            return link
    return "LinkedIn profile not found."
