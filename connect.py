#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, json, websocket, time, ssl
import _thread as thread
from RingBuffer import *
from AggregatedBook import AggregatedBookRequest, AggregatedBookType
from AggregatedBookAnalytics import *
from Book import BookRequest, BookType
from MarketRanking import MarketRankingRequest, MarketRankingType
from Quote import QuoteRequest, QuoteType
from QuoteTrade import QuoteTradeRequest, QuoteTradeType
from ResumeMarket import ResumeMarketListRequest, ResumeMarketType

###### reading configuration
HOME = os.path.dirname(os.path.abspath(__file__))
with open('config.json', "r") as config_json_file:
    cfg = json.load(config_json_file)

###### buffers
BUFFER_SIZE = 10*60*10  # ~10 min
analytic_buffer=RingBuffer(BUFFER_SIZE)

symbol = "petr4" # petr4, bpac11
market = "XBSP" # XBSP := Bovespa, XBMF := BM&F || https://www.onixs.biz/fix-dictionary/4.4/app_6_c.html

def on_message(ws, raw_message):
    data =  json.loads(raw_message)
    if 'type' in data:
        if data['type'] == 'QuoteType':
            quote = QuoteType(data)
            quote.print()
        elif data['type'] == 'AggregatedBookType':
            book = AggregatedBookType(data)
            #book.print()
            analytics = AggregatedBookAnalytics(book)
            analytic_buffer.append(analytics)
            if analytic_buffer.len() > BUFFER_SIZE/2:
                print("process ...")
            analytics.print()
        elif data['type'] == 'BookSnapshotType':
            book = BookType(data)
            book.print()
        elif data['type'] == 'MarketRankingType':
            mrt = MarketRankingType(data)
            mrt.print()
        elif data['type'] == 'ResumeMarketType':
            rmt = ResumeMarketType(data)
            rmt.print()
        elif data['type'] == 'BusinessBookType':
            qtt = QuoteTradeType(data)
            qtt.print()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

req = []
req.append(AggregatedBookRequest(cfg["TKNWF"], symbol).to_json())
#req.append(QuoteTradeRequest(cfg["TKNWF"], symbol).to_json())
#req.append(MarketRankingRequest(cfg["TKNWF"], "bovespa").to_json())
#req.append(ResumeMarketListRequest(cfg["TKNWF"], "highList").to_json())
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
