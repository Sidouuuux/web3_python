from brownie import accounts, FundMe, MockV3Aggregator, network, config
from scripts.utils import get_account


def deploy_fund_me():
    account = get_account()
    if network.show_active() != "developement":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"Currently in the network {network.show_active()}")
        print(f"Deploying Mock")
        mock_aggregator = MockV3Aggregator.deploy(
            27, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print(f"Mock deployed!")

    fund_me = FundMe.deploy(
        "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e",
        {"from": account},
        publish_source=True,
    )
    print(f"Contract address : {fund_me.address} with {account}")


def get_account():
    if network.show_active() == "developement":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_fund_me()
