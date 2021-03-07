#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

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
if __name__ == "__main__":
    qtr = QuoteTradeRequest("test_token", "test_symbol")
    print(qtr.to_json())
