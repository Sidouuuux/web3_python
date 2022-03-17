from scripts.helful_scrpits import get_account
from brownie import Lottery, accounts, config, network
from web3 import Web3


def deploy_lottery():
    account = get_account(id="sidoux_ropsten")
    lottery_contract = Lottery.deploy()


def main():
    deploy_lottery()
