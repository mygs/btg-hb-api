#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import websocket, json
import _thread as thread
import time
import ssl
from QuoteType import *
from AggregatedBookType import *

SERVER_HOME = os.path.dirname(os.path.abspath(__file__))
###### reading configuration
with open(os.path.join(SERVER_HOME, 'config.json'), "r") as config_json_file:
    cfg = json.load(config_json_file)

symbol = "bpac11" # petr4, bpac11
market = "XBSP" # XBSP|XBMF

def on_message(ws, raw_message):
    data =  json.loads(raw_message)
    if 'type' in data:
        if data['type'] == 'QuoteType':
            quote = QuoteType(data)
            print(json.dumps(quote.__dict__))
        if data['type'] == 'AggregatedBookType':
            book = AggregatedBookType(data)
            book.print()
    #print(data)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

req = []
req.append({"token":cfg["TKNWF"],"module":"quotes","service":"aggregatedBook","parameterGet":symbol,"parameters":{"subsbribetype":"1","delay":"100"}})
req.append({"token":cfg["TKNWF"],"module":"quotes","service":"quote","parameterGet":symbol,"parameters":{"subsbribetype":"1","filter":"0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,36,37,38,39,40,41,42,43,44,45,46,47,48,49,54,57,58,59,64,65,66,67,68,69,70,71,72,82,83,84,85,86,88,89,94,95,97,98,99,100,101,102,103,104,105,107,108,110,112,116,118,121,123,134,135,10097,10098,10099","delay":"100"}})
req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"financialAccountInformationCompl","parameters":{"account":cfg["ACCOUNT"],"market":market,"dispatch":False,"history":True,"omsFilter":False}})
req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"position","parameters":{"account":cfg["ACCOUNT"],"market":market,"history":False,"dispatch":False,"openQtyFilter":0}})
req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"dailyOrder","parameters":{"account":cfg["ACCOUNT"],"market":market,"dispatch":False,"history":True}})
req.append({"token":cfg["TKNWF"],"module":"negotiation","service":"cancelOrderReject","parameters":{"account":cfg["ACCOUNT"],"dispatch":False,"market":market}})

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
