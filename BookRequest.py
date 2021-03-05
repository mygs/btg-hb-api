#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

class BookRequest(Request):
    subsbribetype = "1"
    delay = "50"
    def __init__(self, token, module, symbol):
        Request.__init__(self, token, module, "aggregatedBook")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "delay": self.delay}
if __name__ == "__main__":
    br = BookRequest("test_token", "test_module", "test_symbol")
    print(br.to_json())
