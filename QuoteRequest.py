#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

class QuoteRequest(Request):
    subsbribetype = "1"
    filter = "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,36,37,38,39,40,41,42,43,44,45,46,47,48,49,54,57,58,59,64,65,66,67,68,69,70,71,72,82,83,84,85,86,88,89,94,95,97,98,99,100,101,102,103,104,105,107,108,110,112,116,118,121,123,134,135,10097,10098,10099"
    delay = "50"
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "quote")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "filter": self.filter,
                            "delay": self.delay}
if __name__ == "__main__":
    qr = QuoteRequest("test_token", "test_module", "test_symbol")
    print(qr.to_json())
