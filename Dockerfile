FROM python:3.9.1

RUN apt-get update

COPY requirements.txt /curve-manager/requirements.txt

WORKDIR /curve-manager

RUN pip install -r requirements.txt

ADD . .

# @ dev environment variables for training curves
# ENV ASSET
# ENV TRAINING_LABEL=
# ENV NUMBER_OF_DAYS_FOR_TRAINING_CURVE=
# ENV STRIKE_PERCENTAGE=
# ENV EXPIRATION=

# @dev environment variables for network interactions
# ENV KELLY_PRICER_ADDRESS=
# ENV MNEMONIC=
# ENV WEB3_ALCHEMY_PROJECT_ID=
# ENV NETWORK=

RUN brownie networks set_provider alchemy

CMD brownie run scripts/update_curve_manager.py --network $NETWORK