#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json,time
from Request import *
from prettytable import PrettyTable

class AggregatedBookRequest(Request):
    subsbribetype = "1"
    delay = "800"
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "aggregatedBook")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "delay": self.delay}
class AggregatedBookType:

    def __init__(self, message):
        self.timestamp = int(time.time())
        self.symbol = message['parameter']
        self.type = message['type']
        self.bid = message['book']['A']
        self.ask = message['book']['B']

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
    br = AggregatedBookRequest("test_token", "test_symbol")
    print(br.to_json())
    with open('example/aggregatedbook.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    abt.print()
