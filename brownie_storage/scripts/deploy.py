from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # import account from brownie
    account = accounts[0]
    # deploy a contract (import it before)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(updated_value)
    # import account from .env
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # import account from brownie-config.yaml
    # account = accounts.add(config["wallets"]["from_key"])
    # import account from brownie cli
    # account = accounts.load("sidoux_ropsten")


def main():
    print("Deploying contract...")
    deploy_simple_storage()
