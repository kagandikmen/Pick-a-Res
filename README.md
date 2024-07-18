# Pick-a-Res

This is a GUI tool which gathers actual component data from

[DigiKey Product Information V4 API](https://developer.digikey.com/products/product-information-v4)

to help electrical engineers pick resistors for the voltage dividers in their designs.

## Setup

Before using it for the first time, create two .txt files in the root directory with the names ```clientid.txt``` and ```clientsecret.txt```, where you should paste the Client ID and the Client Secret of your DigiKey Production App respectively. It is free to create a Production App on the DigiKey Developer Portal.

## Dependencies

PySide6\
PyQt6\
requests

## Current Status of the Project

This project is still under development as of 2024-07-18. 

## Known Issues

- The API can currently access USA-specific (US, en, USD) data only. 
- Filtering components is not implemented yet, except for the "In Stock" & "RoHS Compliant" filters. 
- The search may not work correctly for all resistor types, but is well tested for through-hole & chip SMT resistors. 
- The GUI still has slight user experience issues.

## Contributing

Pull requests, suggestions, bug fixes etc. are all welcome.

## License

MIT License