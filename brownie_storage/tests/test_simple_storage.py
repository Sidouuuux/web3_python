from brownie import accounts, SimpleStorage


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    storage_value = simple_storage.retrieve()
    expected = 0
    assert storage_value == expected


def test_store():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    update_value = simple_storage.store(27, {"from": account})
    expected = 27
    assert expected == simple_storage.retrieve()
