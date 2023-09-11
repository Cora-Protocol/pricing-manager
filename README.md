# Cora Curve Manager

This repository contains a curve manager docker image that is easy to host and setup.

### Get started

```
$ git clone https://github.com/Cora-Protocol/curve-manager.git

$ pip install -r requirements.txt

```

Create a .env file (see .env.example)

The minimum environment variables required are:

- ASSET=<any coin id, i.e near, eth as listed [here](https://www.coingecko.com/en/api/documentation) >
- WEB3_ALCHEMY_PROJECT_ID=<YOUR_ALCHEMY_PROJECT_ID>
- NETWORK=<the network id as specified [here](https://github.com/eth-brownie/brownie/blob/master/brownie/data/network-config.yaml)>
- KELLY_PRICER_ADDRESS=<KELLY_PRICER_ADDRESS>
- MNEMONIC=<YOUR_MNEMONIC>

Then change the default provider for alchemy by running:

```
$ brownie networks set_provider alchemy
```

### All environment variables

- ASSET
- TRAINING_LABEL
- NUMBER_OF_DAYS_FOR_TRAINING_CURVE
- STRIKE_PERCENTAGE
- EXPIRATION
- NETWORK
- WEB3_ALCHEMY_PROJECT_ID
- KELLY_PRICER_ADDRESS

### Scripts

```
# update the curve
$ brownie run scripts/update_curve_manager.py --network $network
```

### Commands

```
# build docker image
$ docker build -t <tag> .

# run docker image using the .env file
$ docker run --env-file ./env
```
