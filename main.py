import requests
from src.auth import requestToken

def main():
    with open("clientid.txt", 'r') as f:
        clientId = f.read().strip()

    with open("clientsecret.txt", 'r') as f:
        clientSecret = f.read().strip()

    accessToken = requestToken(clientId, clientSecret)

    url = 'https://api.digikey.com/products/v4/search/keyword'

    auth = 'Bearer ' + accessToken
    print(auth)

    headers = {
        'accept': 'application/json',
        'Authorization': auth,
        'X-DIGIKEY-Client-Id': clientId,
        'X-DIGIKEY-Locale-Site': 'US',
        'X-DIGIKEY-Locale-Language': 'en',
        'X-DIGIKEY-Locale-Currency': 'USD',
        'Content-Type': 'application/json'
    }

    data = {
        "Keywords": "100k",
        "Limit": 1,
        "Offset": 0,
    }

    r = requests.post(url, json=data, headers=headers)
    print(r.json())

main()