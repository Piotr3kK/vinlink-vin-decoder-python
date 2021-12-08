# Online VIN decoder - python client

This is an example of python client for VinLink online decoder.

You need to create an account at www.vinlink.com

It's necessary to add some money for production use of service however you may apply for free funds for tests.

Please provide real credentials in main.py
```
client = Client('http://ws.vinlink.com/VLWS/services/Decoder?wsdl', wsse=UsernameToken('login', 'password'))
```
You may decode a sample VIN
```
python main.py 1FMCU04112KA71263
```
```
Model Year: 2002
Make: Ford
Model: Escape
Trim Level: XLT
Engine Type: V6, 3.0L; DOHC 24V; SEFI
Body Type: 4 Door Wagon
Drive Line Type: 4WD
Transmission: 4 speed Automatic / CD4E; 5 speed Manual / G5M
Country = UNITED STATES
Make = Ford
Vehicle Type = Multipurpose Vehicle (MPV)
GVWR Class = Class C: 4,001-5,000 lb
Model = Escape
Engine Type = V6, 3.0L; DOHC 24V; SEFI
Check Digit = 1
Model Year = 2002
Assy. Plant = Kansas City: Claycomo, MO
Production Seq. Number = A71263
Brake System = Hydraulic
Restraint System = Side Air Bag; Air Bag-2nd Generation
Body Type = 4 Door Wagon
Drive Line Type = 4WD
Trim Level = XLT
Vehicle Class = Small MPV
Tonnage = 1/2
Horsepower = 201HP
Fuel Type = Gasoline
Engine Manufacturer = Ford
Manufacturer = Ford Motor Company
Engine Code = 1
Transmission/MfgCode = 4 speed Automatic / CD4E; 5 speed Manual / G5M
AAIA = 11771/69955
AAIA_ENG = 8026
AAIA_LEGACY = 1385276
AAIA_TRANSMISSION` = 742/2452
MPG = A4:16-22-18
VIN = 1FMCU04112KA71263
```
