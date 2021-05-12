import json
import os
import dazl

def main():
    with dazl.simple_client('http://localhost:6865', 'User1') as client:
    # wait for the ACS to be fully read
      client.ready()
      contract_dict = client.find_active('*')
    print(contract_dict)
    print('It is done')

if __name__ == '__main__':
 main()
