#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json
from prettytable import PrettyTable

class MarketRankingType:

    def __init__(self, message):
        self.market = message['parameter']
        self.type = message['type']
        self.ranking = message['marketRanking']['L']


    def print(self):
        ranking = PrettyTable()
        ranking.field_names = ["playerCode",
                            "volumeFinancier",
                            "volumeAmount",
                            "quantityTrade",
                            "type"]
        ranking_length = len(self.ranking)
        for i in range(ranking_length):
           ranking.add_row([self.ranking[i]["PC"],
                            self.ranking[i]["VF"],
                            self.ranking[i]["VA"],
                            self.ranking[i]["QT"],
                            self.ranking[i]["T"]
                        ])
        print(ranking)

if __name__ == "__main__":
    with open('example/marketranking.json', "r") as values_file:
        values_json = json.load(values_file)
    mrt = MarketRankingType(values_json)
    mrt.print()
