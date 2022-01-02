from brownie import accounts, SimpleStorage, network, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())
    pass


def main():
    read_contract()
