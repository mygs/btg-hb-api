#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
from prettytable import PrettyTable
from Request import *

class ResumeMarketListRequest(Request):
    subsbribetype = "1"
    def __init__(self, token, service):
        Request.__init__(self, token, "quotes", service)
        self.parameterGet = "bovespa"
        self.parameters = {"subsbribetype": self.subsbribetype}

class ResumeMarketType:

    def __init__(self, message):
        self.identifier = message['identifier']
        self.type = message['type']
        self.list = message['streamingResumeMarketList']['L']


    def print(self):
        list = PrettyTable()
        print("*****", self.identifier,"*****")
        list.field_names = ["Quote",
                            "Price",
                            "Value",
                            "Date",
                            "volumeFinancier",
                            "C",
                            "QN"]
        list_length = len(self.list)
        for i in range(list_length):
           list.add_row([self.list[i]["Q"],
                            self.list[i]["P"],
                            self.list[i]["V"],
                            self.list[i]["D"],
                            self.list[i]["VF"],
                            self.list[i]["C"],
                            self.list[i]["QN"]
                        ])
        print(list)

if __name__ == "__main__":
    srmlr = ResumeMarketListRequest("test_token", "test_service")
    print(srmlr.to_json())
    with open('example/resumemarketlist.json', "r") as values_file:
        values_json = json.load(values_file)
    rmt = ResumeMarketType(values_json)
    rmt.print()
