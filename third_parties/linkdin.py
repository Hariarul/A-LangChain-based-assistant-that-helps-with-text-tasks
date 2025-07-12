import os
import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("SCRAPIN_API_KEY")
print(apikey)

def scrape_linkedin_profile(Linkedin_profile_url: str, mock: bool = False):
    """Scrape information from LinkedIn profile, using either real API or mock"""
    if mock:
        Linkedin_profile_url = "https://gist.githubusercontent.com/Hariarul/e221d036d08243db06e0390af3d3b7d4/raw/4a2b92cbf7c1a1aa7752e2fa18c6a213ede058cf/haribaskar-scrapin.json"
        response = requests.get(Linkedin_profile_url, timeout=10)
    else:
        api_end_point = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedinUrl": Linkedin_profile_url,  # ✅ correct key name
        }
        response = requests.get(api_end_point, params=params, timeout=10)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text) 
    data = response.json().get("person")
    #data = {
       # k:v
       # for k,v in data.items()
       # if v not in ([],"","",None)
        #and k not in ['schoolName']
    #}
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(Linkedin_profile_url="http://linkedin.com/in/haribaskar-a-a56045301")
    )
