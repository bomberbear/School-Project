import requests

def pull_latest(token, url):
    url = "http://localhost:5000/ebay.api"
    # Replace `YOUR_API_TOKEN` with your actual API token value
    payload = "Toke: "+token

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers, data=payload)


    return response
