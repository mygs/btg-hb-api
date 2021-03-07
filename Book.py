#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable
from Request import *

class BookRequest(Request):
    subsbribetype = "1"
    delay = "100"
    filter = '50'
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "book")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "filter": self.filter,
                            "delay": self.delay}
class BookType:

    def __init__(self, json):
        self.symbol = json['parameter']
        self.type = json['type']
        self.bid = json['book']['A']
        self.ask = json['book']['B']

    def print(self):
        book = PrettyTable()
        book.field_names = ["BID BROKER",
                            "BID TYPE",
                            "BID QTY",
                            "BID $",
                            "ASK $",
                            "ASK QTY",
                            "ASK TYPE",
                            "ASK BROKER"]
        book_length = len(self.bid)
        for i in range(book_length):
           book.add_row([   self.bid[i]["C"],
                            self.bid[i]["T"],
                            self.bid[i]["Q"],
                            self.bid[i]["P"],
                            self.ask[i]["P"],
                            self.ask[i]["Q"],
                            self.ask[i]["T"],
                            self.ask[i]["C"]
                        ])
        print(book)

if __name__ == "__main__":
    br = BookRequest("test_token", "test_symbol")
    print(br.to_json())
    with open('example/book.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = BookType(values_json)
    abt.print()
