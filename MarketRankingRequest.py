#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

class MarketRankingRequest(Request):
    subsbribetype = "1"
    def __init__(self, token, market):
        Request.__init__(self, token, "quotes", "marketRanking")
        self.parameterGet = market
        self.parameters = {"subsbribetype": self.subsbribetype}
if __name__ == "__main__":
    mrr = MarketRankingRequest("test_token", "test_market")
    print(mrr.to_json())
