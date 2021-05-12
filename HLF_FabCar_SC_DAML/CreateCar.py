import json
import logging
import sys
from datetime import date
from os.path import dirname, join

import dazl
from dazl.model.reading import ReadyEvent, ContractCreateEvent

network = dazl.Network()
network.set_config(url='http://localhost:6865')
logging.basicConfig(filename='app.log', level=logging.INFO)

def init_ledger (network: dazl.Network, keyCar, color, make, model, owner, admin, user):
 user_client = network.aio_party(user)
 #Create smart contract
 @user_client.ledger_ready()
 async def init(event: ReadyEvent):
  initcontract = {'owner':owner, 'keyCar': keyCar, 'color': color, 'make': make, 'model': model, 'user' : user_client.party, 'admin' : admin }
  return dazl.create ('FabricFabcarDaml2.InitLedger', initcontract) 

def dazl_main(network):
    
     keyCar = "CAR11"
     color = "red"
     make = "Audi"
     model = "A4"
     owner = "Bob"
     user = "User1" 
     admin = "Admin"
     init_ledger(network, keyCar, color, make, model, owner, user, admin)


def main():
  dazl.run(dazl_main)
    
if __name__ == '__main__':
    main()
