import unittest
import xcat.trades as trades
from xcat.db import DB


class DatabaseTest(unittest.TestCase):

    def setUp(self):
        self.data = {"sell": {"amount": 0.1, "redeemScript": "63a82003d58daab37238604b3e57d4a8bdcffa401dc497a9c1aa4f08ffac81616c22b68876a9147788b4511a25fba1092e67b307a6dcdb6da125d967022a04b17576a914c7043e62a7391596116f54f6a64c8548e97d3fd96888ac", "redeemblocknum": 1066, "currency": "bitcoin", "initiator": "myfFr5twPYNwgeXyjCmGcrzXtCmfmWXKYp", "p2sh": "2MuYSQ1uQ4CJg5Y5QL2vMmVPHNJ2KT5aJ6f", "fulfiller": "mrQzUGU1dwsWRx5gsKKSDPNtrsP65vCA3Z", "fund_tx": "5c5e91a89a08b2d6698f50c9fd9bb2fa22da6c74e226c3dd63d59511566a2fdb"}, "buy": {"amount": 0.2, "redeemScript": "63a82003d58daab37238604b3e57d4a8bdcffa401dc497a9c1aa4f08ffac81616c22b68876a9143ea29256c9d2888ca23de42a8b8e69ca2ec235b167023f0db17576a914c5acca6ef39c843c7a9c3ad01b2da95fe2edf5ba6888ac", "redeemblocknum": 3391, "currency": "zcash", "locktime": 10, "initiator": "tmFRXyju7ANM7A9mg75ZjyhFW1UJEhUPwfQ", "p2sh": "t2HP59RpfR34nBCWH4VVD497tkc2ikzgniP", "fulfiller": "tmTjZSg4pX2Us6V5HttiwFZwj464fD2ZgpY"}, "commitment": "03d58daab37238604b3e57d4a8bdcffa401dc497a9c1aa4f08ffac81616c22b6"}
        self.sell = trades.Contract(self.data['sell'])

    def test_create(self):
        db = DB()
        sell = trades.Contract(self.data['sell'])
        buy = trades.Contract(self.data['buy'])
        trade = trades.Trade(sell, buy, commitment=self.data['commitment'])
        db.create(trade, 'test')

    def test_get(self):
        # trade = db.get('test')
        print("Trade")


if __name__ == '__main__':
    unittest.main()
