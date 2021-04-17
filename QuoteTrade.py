#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json,time
from Request import *
from prettytable import PrettyTable

class QuoteTradeRequest(Request):
    subsbribetype = "1"
    delay = "100"
    quantidade = '15'
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "quoteTrade")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "quantidade": self.quantidade,
                            "delay": self.delay}
class QuoteTradeType:

    def __init__(self, message):
        self.timestamp = int(time.time())
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

    def convert_json_to_csv(self, json_log):
        out_file = json_log + ".csv"
        #with open(out_file, 'w', newline='') as file:
        #    writer = csv.writer(file, delimiter=';')
        #    writer.writerow(['timestamp','symbol'])

            with open(json_log, "r") as values_file:
                for line in values_file:
                    jl = json.loads(line.replace("'", '"'))
                    if ("type" in jl) and (jl["type"] == "BusinessBookType"):
                        #writer.writerow([jl['timestamp'],jl['symbol']])
                        trades = jl['trades']


if __name__ == "__main__":
    #qtr = QuoteTradeRequest("test_token", "test_symbol")
    #print(qtr.to_json())
    #with open('example/quoteTrade.json', "r") as values_file:
    #    values_json = json.load(values_file)
    #qtt = QuoteTradeType(values_json)
    #qtt.print()
    input_args_parser = argparse.ArgumentParser(description='File to be processed')
    input_args_parser.add_argument('File',
                                    nargs='?',
                                    metavar='file',
                                    type=str,
                                    help='json log file')
    args = input_args_parser.parse_args()
    file = args.File
    qtt = QuoteTradeType()
    qtt.convert_json_to_csv(file)
