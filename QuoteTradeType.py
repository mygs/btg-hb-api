#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable

class QuoteTradeType:

    def __init__(self, message):
        self.symbol = message['parameter']
        self.type = message['type']
        self.trades = message['quoteTrade']['L']

    def print(self):
        trades = PrettyTable()
        trades.field_names = ["QTY",
                            "PRICE",
                            "BUY",
                            "TIME",
                            "SELL",
                            "AGRESSOR"]
        for i in range(len(self.trades)):
           trades.add_row([ self.trades[i]["QT"],
                            self.trades[i]["P"],
                            self.trades[i]["PCB"],
                            self.trades[i]["T"],
                            self.trades[i]["PCL"],
                            self.trades[i]["CDA"]
                        ])
        print(trades)

if __name__ == "__main__":
    with open('example/quoteTrade.json', "r") as values_file:
        values_json = json.load(values_file)
    qtt = QuoteTradeType(values_json)
    qtt.print()
