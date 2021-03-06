#!/usr/bin/python3
# -*- coding = utf-8 -*-
from Request import *
import json

class ResumeMarketListRequest(Request):
    subsbribetype = "1"
    def __init__(self, token, service):
        Request.__init__(self, token, "quotes", service)
        self.parameterGet = "bovespa"
        self.parameters = {"subsbribetype": self.subsbribetype}
if __name__ == "__main__":
    srmlr = ResumeMarketListRequest("test_token", "test_service")
    print(srmlr.to_json())
