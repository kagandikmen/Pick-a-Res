# Pick-a-Res

This is a small command-line tool which gathers actual component data from

[DigiKey Product Information V4 API](https://developer.digikey.com/products/product-information-v4)

to help electrical engineers pick resistors for the voltage dividers in their designs.

## Setup

Before using it for the first time, create two .txt files in the root directory with the names ```clientid.txt``` and ```clientsecret.txt```, where you should paste the Client ID and the Client Secret of your DigiKey Sandbox App respectively. It is free to create a Sandbox app on the DigiKey Developer Portal.

## Dependencies

requests

## Current Status of the Project

Only the API calls have been implemented yet.

## Contributing

Pull requests, suggestions, bug fixes etc. are all welcome.

## License

MIT License