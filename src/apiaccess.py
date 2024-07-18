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

        #self.data = {
        #    "Keywords": "string",
        #    "Limit": 0,
        #    "Offset": 0,
        #    "FilterOptionsRequest": {
        #    }
        #}

        self.condo_R1_inCharge = False
        self.condo_R2_inCharge = False
        self.r1Data = {}
        self.r2Data = {}
        self.resistancesInPOhmsDict = {}


    def dataJsonBuilder(self, keyword='string', limit=1, offset=0, resistancesList=[]):
        
        data = {
            "Keywords": keyword,
            "Limit": limit,
            "Offset": offset,
            "FilterOptionsRequest": {
                "CategoryFilter": [
                    {
                        "Id": self.resistorCategoryId
                    }
                ]
            }
        }

        if(len(resistancesList) != 0):
            data['FilterOptionsRequest']['ParameterFilterRequest'] = {
                "CategoryFilter": {
                    "Id": self.resistorCategoryId
                },
                "ParameterFilters": [
                    {
                        "ParameterId": 2085,      # Resistance
                        "FilterValues": [
                            #{
                            #    "Id": "100 µOhms"
                            #},
                        ]
                    }
                ]
            }

        for resistorValue in resistancesList:
            data['FilterOptionsRequest']['ParameterFilterRequest']['ParameterFilters'][0]['FilterValues'].append({'Id': str(resistorValue)})

        return data

    
    def singleAccess(self, dataJson):
        resistorData = requests.post(self.url, json=dataJson, headers=self.headers)
        return resistorData
    
    def resistance2NominalValueInPOhms(self, resstr, *, Round):
        nominal = float(resstr.strip(' pnuµmkMGOhs'))
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

    resistorDataSignal = Signal(dict, dict)

    def sendOverResults(self):
        self.resistorDataSignal.emit(self.r1Data.json(), self.r2Data.json())

    resistorValuesSignal = Signal(list)

    @Slot(int)
    def onResistorCategoryChanged(self, arg):
        self.resistorCategoryId = arg
        resistorValuesList = []
        for filterValue in self.singleAccess(dataJson=self.dataJsonBuilder(keyword='resistor', limit=1)).json()['FilterOptions']['ParametricFilters'][0]['FilterValues']:
            resistorValuesList.append(filterValue['ValueId'])
        
        self.resistorValuesSignal.emit(resistorValuesList)

        for resistance in resistorValuesList:
            val = self.resistance2NominalValueInPOhms(resistance, Round=True)
            if val not in self.resistancesInPOhmsDict:
                self.resistancesInPOhmsDict[val] = [resistance]
            else:
                self.resistancesInPOhmsDict[val].append(resistance)

    @Slot(bool)
    def onInStockSelectionChanged(self, arg):
        pass

    @Slot(bool)
    def onRohsSelectionChanged(self, arg):
        pass

    @Slot(float)
    def onRelationInputChanged(self,arg):
        self.relation = float(arg)

    @Slot(str)
    def onCombo_R1_Changed(self, arg):
        self.condo_R1_inCharge = True
        self.condo_R2_inCharge = False
        self.condo_R1_text = arg
        self.condo_R2_text = ''
    
    @Slot(str)
    def onCombo_R2_Changed(self, arg):
        self.condo_R1_inCharge = False
        self.condo_R2_inCharge = True
        self.condo_R1_text = ''
        self.condo_R2_text = arg

    @Slot()
    def onSearchInitiated(self):
        H = self.relation
        resistorValuesForSearch = []
        if(self.condo_R1_inCharge):
            r1 = self.resistance2NominalValueInPOhms(self.condo_R1_text, Round=False)
            r2 = (H / (1-H)) * r1
            oldResistanceValue = 0
            
            for resistanceValue in self.resistancesInPOhmsDict:
                if(resistanceValue > r2):
                    abs2Bigger = abs(resistanceValue - r2)
                    abs2Smaller = abs(oldResistanceValue - r2)
                    if(abs2Bigger > abs2Smaller):
                        resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue]
                        break
                    elif(abs2Smaller > abs2Bigger):
                        resistorValuesForSearch = self.resistancesInPOhmsDict[resistanceValue]
                        break
                    else:
                        resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue].append(self.resistancesInPOhmsDict[resistanceValue])
                        break
                oldResistanceValue = resistanceValue
            
            if (len(resistorValuesForSearch) == 0):
                resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue]

            r1 = self.resistance2NominalValueInPOhms(self.condo_R1_text, Round=True)
            r1DataJson = self.dataJsonBuilder(keyword='resistor', limit=5, resistancesList=self.resistancesInPOhmsDict[r1])
            r2DataJson = self.dataJsonBuilder(keyword='resistor', limit=5, resistancesList=resistorValuesForSearch)
            
            self.r1Data = self.singleAccess(dataJson=r1DataJson)
            self.r2Data = self.singleAccess(dataJson=r2DataJson)

        elif(self.condo_R2_inCharge):
            r2 = self.resistance2NominalValueInPOhms(self.condo_R2_text, Round=False)
            r1 = ((1-H) / H) * r2
            oldResistanceValue = 0
            
            for resistanceValue in self.resistancesInPOhmsDict:
                if(resistanceValue > r1):
                    abs2Bigger = abs(resistanceValue - r1)
                    abs2Smaller = abs(oldResistanceValue - r1)
                    if(abs2Bigger > abs2Smaller):
                        resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue]
                        break
                    elif(abs2Smaller > abs2Bigger):
                        resistorValuesForSearch = self.resistancesInPOhmsDict[resistanceValue]
                        break
                    else:
                        resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue].append(self.resistancesInPOhmsDict[resistanceValue])
                        break
                oldResistanceValue = resistanceValue
            
            if (len(resistorValuesForSearch) == 0):
                resistorValuesForSearch = self.resistancesInPOhmsDict[oldResistanceValue]

            r2 = self.resistance2NominalValueInPOhms(self.condo_R2_text, Round=True)
            r1DataJson = self.dataJsonBuilder(keyword='resistor', limit=5, resistancesList=resistorValuesForSearch)
            r2DataJson = self.dataJsonBuilder(keyword='resistor', limit=5, resistancesList=self.resistancesInPOhmsDict[r2])
            
            self.r1Data = self.singleAccess(dataJson=r1DataJson)
            self.r2Data = self.singleAccess(dataJson=r2DataJson)

        self.sendOverResults()

    @Slot()
    def onFiltersClicked(self):
        pass