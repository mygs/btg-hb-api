#!/usr/bin/python3
# -*- coding = utf-8 -*-
import json, time
from prettytable import PrettyTable
from Request import *

class QuoteRequest(Request):
    subsbribetype = "1"
    filter = "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,36,37,38,39,40,41,42,43,44,45,46,47,48,49,54,57,58,59,64,65,66,67,68,69,70,71,72,82,83,84,85,86,88,89,94,95,97,98,99,100,101,102,103,104,105,107,108,110,112,116,118,121,123,134,135,10097,10098,10099"
    delay = "500"
    def __init__(self, token, symbol):
        Request.__init__(self, token, "quotes", "quote")
        self.parameterGet = symbol
        self.parameters = {"subsbribetype": self.subsbribetype,
                            "filter": self.filter,
                            "delay": self.delay}
class QuoteType:
    def __init__(self, json):
        self.timestamp = int(time.time())
        values = json['values']
        self.symbol = json['parameter']
        self.type = json['type']
        #self.errorMessage = values.get("-1",None)
        self.timeUpdate = values.get("0",None)
        self.dateTrade = values.get("1",None)
        self.lastTrade = values.get("2",None)
        self.bid = values.get("3",None)
        self.ask = values.get("4",None)
        self.hourLastTrade = values.get("5",None)
        self.quantityLast = values.get("7",None)
        self.quantity = values.get("8",None)
        self.volumeAmount = values.get("9",None)
        self.volumeFinancier = values.get("10",None)
        self.high = values.get("11",None)
        self.low = values.get("12",None)
        self.previous = values.get("13",None)
        self.open = values.get("14",None)
        self.buyTime = values.get("15",None)
        self.sellTime = values.get("16",None)
        self.volumeBetterBid = values.get("19",None)
        self.volumeBetterAsk = values.get("20",None)
        self.variation = values.get("21",None)
        self.soldQuantity = 0
        self.average = values.get("42",None)
        self.marketType = values.get("44",None)
        self.assetType = values.get("45",None)
        self.assetTypeName = self.get_asset_type_name(values.get("45",None))
        self.loteDefault = values.get("46",None)
        self.description = "-" if values.get("47",None)=='' else values.get("47",None)
        self.classification = "-" if values.get("48",None)=='' else values.get("48",None)
        self.quotationForm = values.get("49",None)
        self.directionUnansweredQty = values.get("56",None)
        self.unansweredQty = values.get("57",None)
        self.timeToOpen = values.get("58",None)
        self.timeReprogrammedToOpen = values.get("59",None)
        self.expirationDate = values.get("64",None)
        self.expiration = values.get("65",None)
        self.quantitySymbol = values.get("66",None)
        self.inTheWeek = values.get("67",None)
        self.inTheYear = values.get("68",None)
        self.inTheMonth = values.get("69",None)
        self.status = values.get("84",None)
        self.theoryPrice = values.get("82",None)
        self.theoryQuantity = "-" if values.get("83",None)=='' else values.get("83",None)
        self.exercisePrice = values.get("85",None)
        self.mCap = values.get("95",None)
        self.lastTrade7Days = values.get("97",None)
        self.lastTrade1Month = values.get("98",None)
        self.lastTrade1Year = values.get("99",None)
        self.businesDaysToExpirationDate = values.get("101",None)
        self.calendarDaysToExpirationDate = values.get("102",None)
        self.adjustment = values.get("103",None)
        self.previousAdjustPrice = values.get("104",None)
        self.tunnelUpperLimit = values.get("107",None)
        self.tunnelLowerLimit = values.get("108",None)
        self.tickSize = values.get("110",None)
        self.minimumIncrement = values.get("112",None)
        self.coin = values.get("116",None)
        self.contractMultiplier = values.get("123",None)
        self.deltaVolumeCurrentTime = values.get("134",None)
        self.deltaVolumeAccumulatedHour = values.get("135",None)
        self.deltaVolumeDaily = values.get("10094",None)
        self.calculoWeeklyVariation = values.get("10097",None)
        self.calculoMonthlyVariation = values.get("10098",None)
        self.calculoYearlyVariation = values.get("10099",None)
        self.toMainQuoteInfos = None
        self.theoricChange = 100 * (0 if values.get("82",None)=="-" else values.get("82",None)) / (float(values.get("13",None).replace(',','.')) - 1)
        self.segment = "-"

    def get_asset_type_name(self, code):
        switcher = {
            "1": "A VISTA",
            "2": "OPCAO",
            "3": "INDICE",
            "4": "COMMODITY",
            "5": "MOEDA",
            "6": "TERMO",
            "7": "FUTURO",
            "8": "LEILAO",
            "9": "BONUS",
            "10": "FRACIONARIO",
            "11": "EXERCICIO DE OPCAO",
            "12": "INDICADOR",
            "13": "ETF",
            "15": "VOLUME",
            "16": "OPCAO SOBRE A VISTA",
            "17": "OPCAO SOBRE FUTURO",
            "18": "ATIVO DE TESTE"
            }
        return switcher.get(code, "-");

    def print(self):
        quote = PrettyTable()
        quote.field_names = ["FIELD", "VALUE"]
        for attribute, value in self.__dict__.items():
            #print(attribute, value)
            quote.add_row([ attribute, value ])
        print(quote)

if __name__ == "__main__":
    qr = QuoteRequest("test_token", "test_symbol")
    print(qr.to_json())
    with open('example/quote.json', "r") as values_file:
        values_json = json.load(values_file)
    qt = QuoteType(values_json)
    qt.print()
