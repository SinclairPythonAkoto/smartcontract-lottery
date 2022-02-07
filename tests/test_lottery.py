# 1x ETH @ 3002.44 usd
# 0.01700 -> 51 usd @ 1x eth
# 170000000000000000 -> 50 usd in wei
# 0.022 -> 66 usd (approx)

from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # assert lottery.getEntranceFee() > Web3.toWei(0.016, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.22, "ether")
