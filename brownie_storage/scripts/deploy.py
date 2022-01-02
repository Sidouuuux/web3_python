from brownie import accounts, SimpleStorage, network, config


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    storage_value = simple_storage.retrieve()
    print(storage_value)
    transaction = simple_storage.store(18, {"from": account})
    transaction.wait(1)
    storage_value = simple_storage.retrieve()
    print(storage_value)


def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
