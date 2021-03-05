#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable

class AggregatedBookType:

    def __init__(self, json):
        self.symbol = json['parameter']
        self.type = json['type']
        self.bid = json['book']['B']
        self.ask = json['book']['A']

    def print(self):
        book = PrettyTable()
        book.field_names = ["BID #",
                            "BID QTY",
                            "BID $",
                            "ASK $",
                            "ASK QTY",
                            "ASK #"]
        book_length = len(self.bid)
        amount_bid = 0
        amount_ask = 0
        for i in range(book_length):
           amount_bid = self.bid[i]["Q"] * self.bid[i]["P"]
           amount_ask = self.ask[i]["Q"] * self.ask[i]["P"]
           book.add_row([   self.bid[i]["QTD"],
                            self.bid[i]["Q"],
                            self.bid[i]["P"],
                            self.ask[i]["P"],
                            self.ask[i]["Q"],
                            self.ask[i]["QTD"]
                        ])
        print(book)
        spread = self.ask[0]["P"] - self.bid[0]["P"]
        amount_total = amount_ask + amount_bid
        print("[spread] bid: $",self.bid[0]["P"], " ask: $", self.ask[0]["P"], "diff: $","{:.2f}".format(spread) )
        print("[amount] bid:","{:.2f}".format(100*amount_bid/amount_total),"%   ask:", "{:.2f}".format(100*amount_ask/amount_total),"%")

if __name__ == "__main__":
    with open('example/book.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    abt.print()
