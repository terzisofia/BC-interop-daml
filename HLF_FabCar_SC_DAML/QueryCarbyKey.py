import json
import os
import dazl
import logging
from asyncio import sleep

import dazl

network = dazl.Network()
def main():

 with dazl.simple_client('http://localhost:6865', 'User1') as client:
    # wait for the ACS to be fully read
    client.ready()
    allContracts = client.find(template = "FabricFabcarDaml2.InitLedger")
    for contract in allContracts:
      if contract.cdata ["keyCar"] == "CAR0":
        print("The query is" )
        print(contract.cdata)

if __name__ == '__main__':
    main()
