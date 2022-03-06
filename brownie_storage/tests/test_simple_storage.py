from cmath import exp
from brownie import accounts, config, SimpleStorage


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    expected = 0

    # testing
    assert stored_value == expected


def test_update_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected = 9
    transaction = simple_storage.store(expected, {"from": account})
    transaction.wait(1)
    # testing
    assert expected == simple_storage.retrieve()
