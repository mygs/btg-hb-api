#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json,time, csv, argparse
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

    def __init__(self, message = None):
        self.timestamp = int(time.time())
        if message is not None:
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

    def convert_json_to_csv(self, json_log):
        out_file = json_log + ".csv"
        with open(out_file, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['timestamp','symbol',
                            'b01q','b01p','b01o','b02q','b02p','b02o','b03q','b03p','b03o',
                            'b04q','b04p','b04o','b05q','b05p','b05o','b06q','b06p','b06o',
                            'b07q','b07p','b07o','b08q','b08p','b08o','b09q','b09p','b09o',
                            'b10q','b10p','b10o','b11q','b11p','b11o','b12q','b12p','b12o',
                            'b13q','b13p','b13o','b14q','b14p','b14o','b15q','b15p','b15o',
                            'a01q','a01p','a01o','a02q','a02p','a02o','a03q','a03p','a03o',
                            'a04q','a04p','a04o','a05q','a05p','a05o','a06q','a06p','a06o',
                            'a07q','a07p','a07o','a08q','a08p','a08o','a09q','a09p','a09o',
                            'a10q','a10p','a10o','a11q','a11p','a11o','a12q','a12p','a12o',
                            'a13q','a13p','a13o','a14q','a14p','a14o','a15q','a15p','a15o'
                                ])

            with open(json_log, "r") as values_file:
                for line in values_file:
                    jl = json.loads(line.replace("'", '"'))

                    if ("type" in jl) and (jl["type"] == "AggregatedBookType"):
                        bid = jl['bid']
                        ask = jl['ask']
                        writer.writerow([jl['timestamp'],jl['symbol'],
                        bid[0]['Q'],bid[0]['P'],bid[0]['QTD'],
                        bid[1]['Q'],bid[1]['P'],bid[1]['QTD'],
                        bid[2]['Q'],bid[2]['P'],bid[2]['QTD'],
                        bid[3]['Q'],bid[3]['P'],bid[3]['QTD'],
                        bid[4]['Q'],bid[4]['P'],bid[4]['QTD'],
                        bid[5]['Q'],bid[5]['P'],bid[5]['QTD'],
                        bid[6]['Q'],bid[6]['P'],bid[6]['QTD'],
                        bid[7]['Q'],bid[7]['P'],bid[7]['QTD'],
                        bid[8]['Q'],bid[8]['P'],bid[8]['QTD'],
                        bid[9]['Q'],bid[9]['P'],bid[9]['QTD'],
                        bid[10]['Q'],bid[10]['P'],bid[10]['QTD'],
                        bid[11]['Q'],bid[11]['P'],bid[11]['QTD'],
                        bid[12]['Q'],bid[12]['P'],bid[12]['QTD'],
                        bid[13]['Q'],bid[13]['P'],bid[13]['QTD'],
                        #bid[14]['Q'],bid[14]['P'],bid[14]['QTD'],
                        ask[0]['Q'],ask[0]['P'],ask[0]['QTD'],
                        ask[1]['Q'],ask[1]['P'],ask[1]['QTD'],
                        ask[2]['Q'],ask[2]['P'],ask[2]['QTD'],
                        ask[3]['Q'],ask[3]['P'],ask[3]['QTD'],
                        ask[4]['Q'],ask[4]['P'],ask[4]['QTD'],
                        ask[5]['Q'],ask[5]['P'],ask[5]['QTD'],
                        ask[6]['Q'],ask[6]['P'],ask[6]['QTD'],
                        ask[7]['Q'],ask[7]['P'],ask[7]['QTD'],
                        ask[8]['Q'],ask[8]['P'],ask[8]['QTD'],
                        ask[9]['Q'],ask[9]['P'],ask[9]['QTD'],
                        ask[10]['Q'],ask[10]['P'],ask[10]['QTD'],
                        ask[11]['Q'],ask[11]['P'],ask[11]['QTD'],
                        ask[12]['Q'],ask[12]['P'],ask[12]['QTD'],
                        ask[13]['Q'],ask[13]['P'],ask[13]['QTD']
                        #ask[14]['Q'],ask[14]['P'],ask[14]['QTD']
                        ])

if __name__ == "__main__":
    #br = AggregatedBookRequest("test_token", "test_symbol")
    #print(br.to_json())
    #with open('example/aggregatedbook.json', "r") as values_file:
    #    values_json = json.load(values_file)
    #abt = AggregatedBookType(values_json)
    #abt.print()
    # Add the arguments
    input_args_parser = argparse.ArgumentParser(description='File to be processed')
    input_args_parser.add_argument('File',
                                    nargs='?',
                                    metavar='file',
                                    type=str,
                                    help='json log file')
    args = input_args_parser.parse_args()
    file = args.File
    abt = AggregatedBookType()
    abt.convert_json_to_csv(file)
