import json
from PySide6.QtCore import QObject, Signal, Slot
import requests
from src.auth import requestToken

class ApiAccess(QObject):
    def __init__(self):
        
        with open("clientid.txt", 'r') as f:
            clientId = f.read().strip()

        with open("clientsecret.txt", 'r') as f:
            clientSecret = f.read().strip()

        self.accessToken = requestToken(clientId, clientSecret)
        auth = 'Bearer ' + self.accessToken
        self.url = 'https://api.digikey.com/products/v4/search/keyword'

        self.headers = {
            'accept': 'application/json',
            'Authorization': auth,
            'X-DIGIKEY-Client-Id': clientId,
            'X-DIGIKEY-Locale-Site': 'US',
            'X-DIGIKEY-Locale-Language': 'en',
            'X-DIGIKEY-Locale-Currency': 'USD',
            'Content-Type': 'application/json'
        }

        self.data = {
            "Keywords": "100k",
            "Limit": 5,
            "Offset": 0,
            "FilterOptionsRequest": {
            }
        }
    
    def access(self):
        self.resistorData = requests.post(self.url, json=self.data, headers=self.headers)

    @Slot(int)
    def onResistorCategoryChanged(self, arg):
        self.data["FilterOptionsRequest"]["CategoryFilter"] = [
            {
                "Id": str(arg)
            }     
        ]

    @Slot(int)
    def onInStockSelectionChanged(self, arg):
        self.shouldBeOnStock = arg

    @Slot(float)
    def onRelationInputChanged(self,arg):
        self.relation = arg

    @Slot(str)
    def onApproxValueInputChanged(self, arg):
        self.approxValue = arg

    @Slot(bool)
    def onDoesNotMatterButtonToggled(self, arg):
        self.approxValueDoesNotMatter = arg

    @Slot()
    def onSearchInitiated(self):
        self.access()
        print(self.resistorData.json())