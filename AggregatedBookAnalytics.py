#!/usr/bin/python3
# -*- coding = utf-8 -*-
from AggregatedBookType import *
from prettytable import PrettyTable

class AggregatedBookAnalytics:
    def __init__(self, book):
        self.book = book
        self.spread = 0
        self.best_bid_price = 0
        self.best_ask_price = 0
        self.pressure_ask = 0
        self.pressure_bid = 0
        self.weighted_bid_price = 0
        self.weighted_ask_price = 0
        self.weighted_price = 0
        self.calc()

    def calc(self):
        book_length = len(self.book.bid)
        volume_bid = 0
        volume_ask = 0
        total_qty_bid = 0
        total_qty_ask = 0

        for i in range(book_length):
            bid = self.book.bid[i]
            ask = self.book.ask[i]
            volume_bid = volume_bid + bid["Q"] * bid["P"]
            volume_ask = volume_ask + ask["Q"] * ask["P"]
            total_qty_bid = total_qty_bid + bid["Q"]
            total_qty_ask = total_qty_ask + ask["Q"]

        self.best_bid_price = self.book.bid[0]["P"]
        self.best_ask_price = self.book.ask[0]["P"]
        self.spread =  self.best_ask_price - self.best_bid_price
        volume_total = volume_ask + volume_bid
        self.pressure_ask = 100*volume_ask/volume_total
        self.pressure_bid = 100*volume_bid/volume_total
        self.weighted_bid_price = volume_bid/total_qty_bid
        self.weighted_ask_price = volume_ask/total_qty_ask
        self.weighted_price = (volume_bid + volume_ask)/(total_qty_bid + total_qty_ask)

    def print(self):
        summary = PrettyTable()
        summary.field_names = ["ANALYTIC", "RESULT"]
        summary.add_row([ "Bid/Ask Spread $", '{0:.2f}'.format(self.spread)])
        summary.add_row([ "Weighted Price $", '{0:.2f}'.format(self.weighted_price)])
        summary.add_row([ "Best Bid $", self.best_bid_price])
        summary.add_row([ "Best Ask $", self.best_ask_price])
        summary.add_row([ "Balance Bid %", '{0:.2f}'.format(self.pressure_bid)])
        summary.add_row([ "Balance Ask %", '{0:.2f}'.format(self.pressure_ask)])
        summary.add_row([ "Weighted Bid $", '{0:.2f}'.format(self.weighted_bid_price)])
        summary.add_row([ "Weighted Ask $", '{0:.2f}'.format(self.weighted_ask_price)])
        print(summary)


if __name__ == "__main__":
    with open('example/aggregatedbook.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    analytics = AggregatedBookAnalytics(abt)

    analytics.print()
