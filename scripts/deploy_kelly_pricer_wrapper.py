#!/usr/bin/python3

from brownie import KellyPricerWrapper, accounts


def main():
    return KellyPricerWrapper.deploy({'from': accounts[0]})
