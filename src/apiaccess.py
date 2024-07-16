import json
from PySide6.QtCore import QObject, Signal, Slot
import requests
from src.auth import requestToken

class ApiAccess(QObject):
    def __init__(self):
        super(ApiAccess, self).__init__()

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
            "Keywords": "string",
            "Limit": 0,
            "Offset": 0,
            "FilterOptionsRequest": {
            }
        }
    
    def singleAccess(self, keyword, limit):

        self.data['Keywords'] = keyword
        self.data['Limit'] = limit

        resistorData = requests.post(self.url, json=self.data, headers=self.headers)
        return resistorData

    def doubleAccess(self):
        pass
        #if(self.approxIsR1):

        #elif(self.approxIsR2):

    def keywordTransformer(keyword):
        pass
    
    def resistance2NominalValueInPOhms(self, resstr, Round):
        nominal = float(resstr.strip('pnuµmkMGOhs'))
        if(Round):
            match(resstr[-5]):
                case 'p':
                    return nominal
                case 'n':
                    return round(nominal * 10e3, -1)
                case 'u' | 'µ':
                    return round(nominal * 10e6, -4)
                case 'm':
                    return round(nominal * 10e9, -7)
                case 'k':
                    return round(nominal * 10e15, -13)
                case 'M':
                    return round(nominal * 10e18, -16)
                case 'G':
                    return round(nominal * 10e21, -19)
                case " ":
                    return round(nominal * 10e12, 10)
                case _:
                    return 'Error!'
        else:
            match(resstr[-5]):
                case 'p':
                    return nominal
                case 'n':
                    return nominal * 10e3
                case 'u' | 'µ':
                    return nominal * 10e6
                case 'm':
                    return nominal * 10e9
                case 'k':
                    return nominal * 10e15
                case 'M':
                    return nominal * 10e18
                case 'G':
                    return nominal * 10e21
                case ' ':
                    return nominal * 10e12
                case _:
                    return "Error!"


    resistorValuesSignal = Signal(list)

    @Slot(int)
    def onResistorCategoryChanged(self, arg):
        self.data["FilterOptionsRequest"]["CategoryFilter"] = [
            {
                "Id": arg
            }     
        ]
        resistorValuesList = []
        for filterValue in self.singleAccess('resistor', 1).json()['FilterOptions']['ParametricFilters'][0]['FilterValues']:
            resistorValuesList.append(filterValue['ValueId'])
        
        self.resistorValuesSignal.emit(resistorValuesList)

        resistancesInPOhmsDict = {}
        for resistance in resistorValuesList:
            val = self.resistance2NominalValueInPOhms(resistance, True)
            if val not in resistancesInPOhmsDict:
                resistancesInPOhmsDict[val] = [resistance]
            else:
                resistancesInPOhmsDict[val].append(resistance)

    @Slot(bool)
    def onInStockSelectionChanged(self, arg):
        self.shouldBeInStock = arg

    @Slot(bool)
    def onRohsSelectionChanged(self, arg):
        self.shouldBeRohs = arg

    @Slot(float)
    def onRelationInputChanged(self,arg):
        self.relation = float(arg)

    @Slot(str)
    def onCombo_R1_Changed(self, arg):
        pass
    
    @Slot(str)
    def onCombo_R2_Changed(self, arg):
        pass

    @Slot()
    def onSearchInitiated(self):
        self.doubleAccess()
        #print(self.resistorData.json())

    @Slot()
    def onFiltersClicked(self):
        pass