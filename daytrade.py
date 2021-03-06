#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import websocket, json
import _thread as thread
import time
import ssl
from QuoteType import *
from AggregatedBookType import *
from BookType import *
from MarketRankingType import *
from ResumeMarketListRequest import *
from AggregatedBookRequest import *
from AggregatedBookAnalytics import *
from QuoteRequest import *
from BookRequest import *
from MarketRankingRequest import *


SERVER_HOME = os.path.dirname(os.path.abspath(__file__))
###### reading configuration
with open(os.path.join(SERVER_HOME, 'config.json'), "r") as config_json_file:
    cfg = json.load(config_json_file)

symbol = "petr4" # petr4, bpac11
market = "XBSP" # XBSP := Bovespa, XBMF := BM&F || https://www.onixs.biz/fix-dictionary/4.4/app_6_c.html

def on_message(ws, raw_message):
    data =  json.loads(raw_message)
    if 'type' in data:
        if data['type'] == 'QuoteType':
            quote = QuoteType(data)
            quote.print()
        if data['type'] == 'AggregatedBookType':
            book = AggregatedBookType(data)
            book.print()
            analytics = AggregatedBookAnalytics(book)
            analytics.print()
        if data['type'] == 'BookSnapshotType':
            book = BookType(data)
            book.print()
        if data['type'] == 'MarketRankingType':
            mrt = MarketRankingType(data)
            mrt.print()
        if data['type'] == 'ResumeMarketType':
            print(data)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

req = []
#req.append(AggregatedBookRequest(cfg["TKNWF"], symbol).to_json())
#req.append(MarketRankingRequest(cfg["TKNWF"], "bovespa").to_json())
#req.append(ResumeMarketListRequest(cfg["TKNWF"], "highList").to_json())
req.append(ResumeMarketListRequest(cfg["TKNWF"], "fallList").to_json())
#req.append(ResumeMarketListRequest(cfg["TKNWF"], "highVolumeList").to_json())
#req.append(ResumeMarketListRequest(cfg["TKNWF"], "fallVolumeList").to_json())
#req.append(BookRequest(cfg["TKNWF"], symbol).to_json())
#req.append(QuoteRequest(cfg["TKNWF"], symbol).to_json())
#req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"financialAccountInformationCompl","parameters":{"account":cfg["ACCOUNT"],"market":market,"dispatch":False,"history":True,"omsFilter":False}})
#req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"position","parameters":{"account":cfg["ACCOUNT"],"market":market,"history":False,"dispatch":False,"openQtyFilter":0}})
#req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"dailyOrder","parameters":{"account":cfg["ACCOUNT"],"market":market,"dispatch":False,"history":True}})
#req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"cancelOrderReject","parameters":{"account":cfg["ACCOUNT"],"dispatch":False,"market":market}})

def on_open(ws):
    def run(*args):
        for i in range(len(req)):
            time.sleep(1)
            ws.send(json.dumps(req[i]))
        print("subscription request sent")
    thread.start_new_thread(run, ())

if __name__ == "__main__":
    print("*** STARTING BTG HB DAYTRADE SUPPORT SYSTEM ***")
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(cfg["ENDPOINT"]+cfg["TKNWF"],
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
