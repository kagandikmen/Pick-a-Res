import requests
from src.auth import requestToken

def main():
    with open("clientid.txt", 'r') as f:
        clientId = f.read().strip()

    with open("clientsecret.txt", 'r') as f:
        clientSecret = f.read().strip()

    accessToken = requestToken(clientId, clientSecret)

    url = 'https://sandbox-api.digikey.com/products/v4/search/P5555-ND/productdetails'

    auth = 'Bearer ' + accessToken

    headers = {
        'Authorization': auth,
        'X-DIGIKEY-Client-Id': clientId
    }

    data = {
        'X-DIGIKEY-Locale-Site': 'US',
        'X-DIGIKEY-Locale-Language': 'en',
        'X-DIGIKEY-Locale-Currency': 'USD',
    }

    r = requests.get(url, data=data, headers=headers)
    print(r.json())

main()