import requests  

API_KEY = "YOUR_API_KEY_HERE"

def virustotal_scan(url):
    endpoint = "https://www.virustotal.com/api/v3/urls"

    headers = {
        "x-apikey": API_KEY
    }

    data = {
        "url": url
    }

    response = requests.post(endpoint, headers=headers, data=data)
    print(response.json())
