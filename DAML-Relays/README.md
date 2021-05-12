# DAML on Fabric & Sawtooth

FabcCar app implementation of DAML ledger that stores data transactions using Hyperledger Fabric & Hyperledger Sawtooth

# Quick Start Guide

## Prerequisites

These are the minimal requirements that this flow was tested with. It's good to use greater versions or sometimes even lower, but not advised.
- **Ubuntu** version 18.04
- **Python** version > 3.6
- **Dazl** version > 7.5
- **Pipenv**
- **DAML SDK** version > 0.13.40
- **NodeJS** version 10.16.2
- **docker-compose** version 1.24.0
- **docker CE** version 18.09.6
- **Java / JDK** version 1.8.0
- **Scala** version 2.12.7
- **SBT** version 1.2.8
- **Fabric SDK Java** version 1.4.1
- **Fabric** version 1.4.4

### Deploy DAML FabCar smart contract on Hyperledger Fabric
### Step 1. Start Hyperledger Fabric

```
$ cd /home/iti-696/Desktop/DAML/daml-on-fabric/src/test/fixture
```

```
$ ./restart_fabric.sh
```
### Step 2. Build FabCar project

```
$ cd /home/iti-696/Desktop/DAML/FabCarTrials/SMFabric
```

```
$ daml build
```

### Step 3. Run the Ledger with FabCar DAR 

```
$ cd /home/iti-696/Desktop/DAML/daml-on-fabric
``` 

```
$ sbt "run --port 6865 --role provision,time,ledger,explorer /home/iti-696/Desktop/DAML/FabCarTrials/SMFabric/.daml/dist/FabCar-1.0.0.dar"
```

#### Services, or "Roles"

You may have noticed that the required argument for DAML-on-Fabric is "role".

There are several roles that define which parts of the service are going to be executed:

- `provision`: will connect to Fabric and prepare it to be used as storage for a DAML ledger.
- `ledger`: will run a DAML Ledger API endpoint at a port specified with `--port` argument.
- `time`: will run a DAML time service, which writes heartbeats to the ledger. There should be exactly one time service per ledger.
- `explorer`: will run a block explorer service that exposes a REST API to view the content of blocks and transactions inside the Fabric network for debugging or demonstration purposes. The explorer will run at a port specified in *config.json* file. It provides REST API that responds at endpoints `/blocks[?id=...]` and `/transactions[?id=...]`


### Step 4. Run DAML Navigator

```
$ cd /home/iti-696/Desktop/DAML/FabCarTrials/SMFabric
```

```
$ daml ledger allocate-parties
```

```
$ daml navigator server localhost 6865 --port 7500
```
### Step 5. Interact with python libraries

```
$ cd /home/iti-696/Desktop/DAML/FabCarTrials/Fabric/Python
```

```
$ pipenv run python3 InitLedger.py --url http://localhost:6865
```

```
$ pipenv run python3 ChangeOwner.py --url http://localhost:6865
```

```
$ pipenv run python3 CreateCar.py --url http://localhost:6865
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 6. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:7500/
- Hyperledger Fabric block explorer at http://localhost:8080/blocks
- Hyperledger Fabric block explorer at http://localhost:8080/transactions
- DAML Ledger API endpoint at *localhost:6865*

### Deploy DAML FabCar smart contract on Hyperledger Sawtooth

### 1. Start Hyperlegder Sawtooth network

```
$ cd /home/iti-696/Desktop/DAML/daml-on-sawtooth
```

```
$ export ISOLATION_ID=my-local-build
```

```
$ ./docker/run.sh start
```

### Step 2. Build FabCar project & Run DAML Navigator

```
$ cd /home/iti-696/Desktop/DAML/FabCarTrials/SMSAwtooth
```

```
$ daml build
```

```
$ daml ledger allocate-parties --host localhost --port 9000
```

```
$ daml ledger upload-dar --host localhost --port 9000 
```

```
$ daml ledger navigator --host localhost --port 9000
```

### Step 3. Interact with python libraries

```
$ cd /home/iti-696/Desktop/DAML/FabCarTrials/Sawtooth/Python
```

```
$ pipenv run python3 UpdateLedger.py  --url http://localhost:9000(Optional!! It is executed from fabric when a car is sold)
```

```
$ pipenv run python3 QueryAllCars.py 
```

```
$ pipenv run python3 QueryCarbyKey.py --key <int value>
```

### Step 4. Conclusion

Now you can explore your freshly setup DAML ledger.

You should have the following services running:

- DAML Navigator at http://localhost:4000/
- Hyperledger Fabric block explorer at http://localhost:80/
- DAML Ledger API endpoint at *localhost:9000*

**Note:** If you shut down network and want to use it again you should:
```
$ sudo su
```

```
$ chmod a+rwx /home/iti-696/Desktop/DAML/daml-on-sawtooth/docker/keys
```

```
$ chmod a+rwx /home/iti-696/Desktop/DAML/daml-on-sawtooth/docker/keys/validator.priv
```

```
$ docker container prune 
```

```
$ docker image prune 
```

```
$ docker volume prune
```

```
$ docker network prune
```

