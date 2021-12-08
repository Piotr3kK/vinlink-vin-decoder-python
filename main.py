import sys
from zeep import Client
from zeep.wsse.username import UsernameToken

if __name__ == '__main__':
    client = Client('http://ws.vinlink.com/VLWS/services/Decoder?wsdl', wsse=UsernameToken('login', 'password'))
    for vin in sys.argv[1:]:
        results = client.service.decode(vin, 'BASIC_PLUS')
        if results:
            result = results[0]
            # print main attributes
            print("Model Year: %s" % result.modelYear)
            print("Make: %s" % result.make)
            print("Model: %s" % result.model)
            print("Trim Level: %s" % result.trimLevel)
            print("Engine Type: %s" % result.engineType)
            print("Body Type: %s" % result.bodyType)
            print("Drive Line Type: %s" % result.driveLineType)
            print("Transmission: %s" % result.transmission)
            # print all available attributes
            attributes = result.vinSpecification.Item
            for a in attributes:
                print("%s = %s" % (a.name, a.value))
