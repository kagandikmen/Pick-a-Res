import requests

def requestToken(clientId, clientSecret):
    
    url = 'https://api.digikey.com/v1/oauth2/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'client_id': clientId,
        'client_secret': clientSecret,
        'grant_type': 'client_credentials'
    }

    r = requests.post(url, data=data, headers=headers)
    accessToken = r.json()['access_token']
    return accessToken