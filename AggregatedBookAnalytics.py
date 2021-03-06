#!/usr/bin/python3
# -*- coding = utf-8 -*-
from AggregatedBookType import *
from prettytable import PrettyTable

class AggregatedBookAnalytics:
    def __init__(self, book):
        self.book = book
        self.spread = None
        self.best_bid_price = None
        self.best_ask_price = None
        self.pressure_ask = None
        self.pressure_bid = None
        self.calc()

    def calc(self):
        book_length = len(self.book.bid)
        amount_bid = 0
        amount_ask = 0
        for i in range(book_length):
            bid = self.book.bid[i]
            ask = self.book.ask[i]
            amount_bid = bid["Q"] * bid["P"]
            amount_ask = ask["Q"] * ask["P"]

        self.best_bid_price = self.book.bid[0]["P"]
        self.best_ask_price = self.book.ask[0]["P"]
        self.spread =  self.best_ask_price - self.best_bid_price
        amount_total = amount_ask + amount_bid
        self.pressure_ask = 100*amount_ask/amount_total
        self.pressure_bid = 100*amount_bid/amount_total

    def print(self):
        summary = PrettyTable()
        summary.field_names = ["ANALYTIC", "RESULT"]
        summary.add_row([ "Spread", self.spread])
        summary.add_row([ "Best Bid Price", self.best_bid_price])
        summary.add_row([ "Best Ask Price", self.best_ask_price])
        summary.add_row([ "Bid pressure", self.pressure_bid])
        summary.add_row([ "Ask pressure", self.pressure_ask])
        print(summary)


if __name__ == "__main__":
    with open('example/aggregatedbook.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    analytics = AggregatedBookAnalytics(abt)

    analytics.print()
