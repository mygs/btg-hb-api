#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

class AggregatedBookRequest(Request):
    subsbribetype = "1"
    delay = "100"
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "aggregatedBook")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "delay": self.delay}
if __name__ == "__main__":
    br = AggregatedBookRequest("test_token", "test_symbol")
    print(br.to_json())
