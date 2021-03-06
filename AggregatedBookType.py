#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable

class AggregatedBookType:

    def __init__(self, message):
        self.symbol = message['parameter']
        self.type = message['type']
        self.bid = message['book']['A'] #?
        self.ask = message['book']['B'] #?

    def print(self):
        book = PrettyTable()
        book.field_names = ["BID #",
                            "BID QTY",
                            "BID $",
                            "ASK $",
                            "ASK QTY",
                            "ASK #"]
        book_length = len(self.bid)
        for i in range(book_length):
           book.add_row([   self.bid[i]["QTD"],
                            self.bid[i]["Q"],
                            self.bid[i]["P"],
                            self.ask[i]["P"],
                            self.ask[i]["Q"],
                            self.ask[i]["QTD"]
                        ])
        print(book)

if __name__ == "__main__":
    with open('example/aggregatedbook.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    abt.print()
