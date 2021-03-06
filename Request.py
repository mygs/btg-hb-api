#!/usr/bin/python3
# -*- coding = utf-8 -*-

class Request:
    def __init__(self, token, module, service):
        self.token = token
        self.module = module
        self.service = service
    def to_json(self):
        return self.__dict__
