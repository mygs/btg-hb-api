#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable

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
    with open('example/book.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = BookType(values_json)
    abt.print()
