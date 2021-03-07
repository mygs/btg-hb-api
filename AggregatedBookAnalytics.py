#!/usr/bin/python3
# -*- coding = utf-8 -*-
from AggregatedBookType import *
from prettytable import PrettyTable

class AggregatedBookAnalytics:
    def __init__(self, book):
        self.spread = 0
        self.book_depth = 0
        self.book_imbalance = 0
        self.best_bid_price = 0
        self.best_ask_price = 0
        self.pressure_ask = 0
        self.pressure_bid = 0
        self.weighted_bid_price = 0
        self.weighted_ask_price = 0
        self.weighted_mid_price = 0
        self.weighted_price = 0
        self.middle_price = 0
        self.calc(book)

    def calc(self, book):
        self.book_depth = len(book.bid)
        volume_bid = 0
        volume_ask = 0
        total_qty_bid = 0
        total_qty_ask = 0

        for i in range(self.book_depth):
            bid = book.bid[i]
            ask = book.ask[i]
            volume_bid = volume_bid + bid["Q"] * bid["P"]
            volume_ask = volume_ask + ask["Q"] * ask["P"]
            total_qty_bid = total_qty_bid + bid["Q"]
            total_qty_ask = total_qty_ask + ask["Q"]

        self.best_bid_price = book.bid[0]["P"]
        self.best_ask_price = book.ask[0]["P"]
        #higher liquidity => more shares are offered with less price gaps
        self.spread =  self.best_ask_price - self.best_bid_price
        # Simple average of the best bid and ask
        self.middle_price = (self.best_ask_price + self.best_bid_price)/2
        volume_total = volume_ask + volume_bid
        self.pressure_ask = volume_ask/volume_total
        self.pressure_bid = volume_bid/volume_total
        # Imbalance is a ratio of limit order volumes between the bid and ask side
        self.book_imbalance = (volume_bid - volume_ask)/volume_total
        # Weighted price to combine the price aspect and the quantity aspect of the book
        self.weighted_bid_price = volume_bid/total_qty_bid
        self.weighted_ask_price = volume_ask/total_qty_ask
        # Weighted average mid-quote
        self.weighted_mid_price = (book.bid[0]["P"]*book.bid[0]["Q"] + book.ask[0]["P"]*book.ask[0]["Q"])/(book.bid[0]["Q"] + book.ask[0]["Q"])
        self.weighted_price = (volume_bid + volume_ask)/(total_qty_bid + total_qty_ask)

    def print(self):
        summary = PrettyTable()
        summary.field_names = ["ANALYTIC", "RESULT"]
        summary.add_row([ "Bid/Ask Spread $", '{0:.3f}'.format(self.spread)])
        summary.add_row([ "Book depth", self.book_depth])
        summary.add_row([ "Book Imbalance", '{0:.3f}'.format(self.book_imbalance)])
        summary.add_row([ "===", '==='])
        summary.add_row([ "Balance Ask %", '{0:.3f}'.format(self.pressure_ask)])
        summary.add_row([ "Weighted Ask $", '{0:.3f}'.format(self.weighted_ask_price)])
        summary.add_row([ "Best Ask $", self.best_ask_price])
        summary.add_row([ "vvv", "vvv"])
        summary.add_row([ "Weighted Price $", '{0:.3f}'.format(self.weighted_price)])
        summary.add_row([ "Weighted Mid Price $", '{0:.3f}'.format(self.weighted_mid_price)])
        summary.add_row([ "Middle Price $", '{0:.3f}'.format(self.middle_price)])
        summary.add_row([ "^^^", "^^^"])
        summary.add_row([ "Best Bid $", self.best_bid_price])
        summary.add_row([ "Weighted Bid $", '{0:.3f}'.format(self.weighted_bid_price)])
        summary.add_row([ "Balance Bid %", '{0:.3f}'.format(self.pressure_bid)])


        print(summary)


if __name__ == "__main__":
    with open('example/aggregatedbook.json', "r") as values_file:
        values_json = json.load(values_file)
    abt = AggregatedBookType(values_json)
    analytics = AggregatedBookAnalytics(abt)

    analytics.print()
