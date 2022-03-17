from brownie import SimpleStorage, accounts, config


def read_contract():
    # select the most recent deployment from the deployment folder
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    read_contract()
