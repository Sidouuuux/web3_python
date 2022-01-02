from eth_account import account
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import web3
from dotenv import load_dotenv
import os

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

abi = json.loads(
    compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["metadata"]
)["output"]["abi"]

w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/e2e0f08d3ad64d5f8e5c2105114f8901")
)
chain_id = 4
account_address = "0x43B5E32f1616b81575dbC2AAD02695f3FB8d1447"
account_key = os.getenv("ACCOUNT_KEY")
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

nonce = w3.eth.getTransactionCount(account_address)

print("Creating transaction")
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": account_address,
        "nonce": nonce,
    }
)
print("Signing transaction")
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=account_key)

print("Deploying contract")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed contract")
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
print(simple_storage.functions.retrieve().call())

store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": account_address,
        "nonce": nonce + 1,
    }
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=account_key
)
tx_store_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
print("Updating stored Value")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_store_hash)
print("Transaction receipt : " + str(tx_receipt))

print("Result : " + str(simple_storage.functions.retrieve().call()))
