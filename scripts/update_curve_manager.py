#!/usr/bin/python3

import os
from brownie import KellyPricerWrapper, accounts
from libs.curve_gen.kelly import evaluate_premium_curve
from libs.historic_downloader import historic_downloader
from libs.utils import create_input_file
from libs.curve_gen.utils import build_generator_config
from libs.curve_gen.gen import Generator
from libs.curve_config import curve_config, curve_defaults
from dotenv import load_dotenv

load_dotenv()

PATH = 'inputs'


def get_curve_parameters(config):
    # download historical
    hd = historic_downloader.HistoricDownloader()
    hd.download_history_file(
        PATH, config.asset, config.number_of_days_for_training_curve)

    default_curve_config = f'{PATH}/CurveConfigFor{config.asset.title()}.csv'
    price_history_file = f'{PATH}/{config.asset}.csv'
    create_input_file.create_input_file(price_history_file, PATH, config)

    gen = Generator()
    gen.configure_curve_gen(build_generator_config(
        default_curve_config, price_history_file))
    curve_df, pdf_df, training_df = gen.generate_curves()
    abcd_result = [curve_df.loc[0, 'A'], curve_df.loc[0, 'B'],
                   curve_df.loc[0, 'C'], curve_df.loc[0, 'D']]
    return abcd_result


def get_config():
    # get default config
    default_config = curve_defaults.ConfigDefault()

    # get config from environment variables or use defaults
    asset = os.environ.get('ASSET')

    training_label = os.environ.get(
        'TRAINING_LABEL', default_config.training_label)

    number_of_days_for_training_curve = os.environ.get(
        'NUMBER_OF_DAYS_FOR_TRAINING_CURVE', default_config.number_of_days_for_training_curve)

    strike_percentage = os.environ.get(
        'STRIKE_PERCENTAGE', default_config.strike_percentage)

    expiration = os.environ.get('EXPIRATION', default_config.expiration)

    config = curve_config.Config(
        asset,
        number_of_days_for_training_curve,
        strike_percentage,
        expiration,
        training_label
    )
    return config


def main():
    # get config
    config = get_config()

    print("Starting Curve Manager For:", config.asset)

    # network
    network = os.environ.get("NETWORK")
    print("Network:", network)

    a, b, c, d = get_curve_parameters(config)
    print("Curve Parameters")
    print('A: ', a)
    print('B: ', b)
    print('C: ', c)
    print('D: ', d)

    # get account
    mnemonic = os.environ.get('MNEMONIC')
    account = accounts.from_mnemonic(mnemonic)

    # contract instance
    contract_address = os.environ.get("KELLY_PRICER_ADDRESS")
    kelly_wrapper = KellyPricerWrapper.at(contract_address)

    kelly_wrapper.updateCurve(a, b, c, d, {'from': account})
