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

def init_ledger (network: dazl.Network, keyCar, admin, newOwner, user):
	user_client = network.aio_party(user)
 #Create smart contract
 
	@user_client.ledger_ready()
	async def init(event: ContractCreateEvent):
	 allContracts =user_client.find(template = "FabricFabcarDaml2.InitLedger")
	 for contract in allContracts:
			if contract.cdata ["keyCar"] == keyCar:
				#print("The query is" )
				#print(contract.cdata)
				fromdictcolor = contract.cdata["color"]
				fromdictmake = contract.cdata["make"]
				fromdictmodel = contract.cdata["model"]
				fromdictowner = contract.cdata["owner"]
	 return dazl.exercise(contract.cid, 'Newowner', {'newOwner': newOwner})		
	 #return dazl.create ('FabricFabcarDaml2.InitLedger',{'owner' : fromdictowner, 'keyCar': keyCar, 'color': fromdictcolor, 'make': fromdictmake, 'model': fromdictmodel, 'user': user_client.party, 'admin': admin}) 
		#return dazl.create ('FabricFabcarDaml2.InitLedger',{contract.cdata})
	 

def dazl_main(network):
		 newOwner = "Alice"
		 keyCar = "CAR0"
		 user = "User1" 
		 admin = "Admin"
		 init_ledger(network, keyCar, admin, newOwner, user)


def main():
	dazl.run(dazl_main)
		
if __name__ == '__main__':
		main()
