# Cora Pricing Manager

This repository contains a pricing manager implemention for the different pricing models supported in the Cora protocol.

Supported pricing models:

- Black Scholes
- Fixed Rate
- Kelly

The repository contains a dockerized version for easy setup in the Cloud or any machine with docker installed.

### Get started

```
$ git clone https://github.com/Cora-Protocol/pricing-manager.git

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
