#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

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
if __name__ == "__main__":
    br = BookRequest("test_token", "test_symbol")
    print(br.to_json())
