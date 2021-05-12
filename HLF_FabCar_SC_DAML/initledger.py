import csv
import pandas as pd
import numpy
import json
import logging
import os
import sys
import time
from datetime import date
from os.path import dirname, join

import dazl
from dazl.model.reading import ReadyEvent, ContractCreateEvent

network = dazl.Network()
network.set_config(url='http://localhost:6865')
logging.basicConfig(filename='app.log', level=logging.INFO)

def init_ledger (network: dazl.Network, keyCar, color, make, model, owner, user, admin):
 user_client = network.aio_party(user)
 #Create smart contract
 @user_client.ledger_ready()
 async def init(event: ReadyEvent):
   logging.info ("Initializing car for" + owner)
   initcontract = {'owner':owner, 'keyCar': keyCar, 'color': color, 'make': make, 'model': model, 'user' : user_client.party, 'admin' : admin }
   return dazl.create ('FabricFabcarDaml2.InitLedger', initcontract) 

def dazl_main(network):
    data = pd.read_csv('FabricCars.csv')
    colorcsv = data[['color']].values.tolist()
    makecsv = data[['make']].values.tolist()
    modelcsv = data[['model']].values.tolist()
    ownercsv = data[['owner']].values.tolist()
    #Convert lists to strings
    for x in range(0, 10):
     keyCar = "CAR" + str(x)
     color = ''.join(str(e) for e in colorcsv[x])
     make = ''.join(str(e) for e in makecsv[x])
     model = ''.join(str(e) for e in modelcsv[x])
     owner = ''.join(str(e) for e in ownercsv[x])
     user = "User1" 
     admin = "Admin"
     init_ledger(network, keyCar, color, make, model, owner, user, admin)


def main():
  dazl.run(dazl_main)
    
if __name__ == '__main__':
    main()
