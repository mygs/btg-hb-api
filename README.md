# BTGPactual Home Broker 3rd party api

This is a Python api to connect with BTGPactual Web Home Broker. This api enables users to develop their own tools to support theirs trading strategies.

## Configuration keys
Create config.json file, just like bellow:
```json
{
  "SYMBOLS": ["?????"],
  "ACCOUNT": "?????",
  "TKNWF": "?????",
  "ENDPOINT": "wss://webfeeder.btgpactual.com/ws?reconnect="
}
```
replace "?????" accordingly:
| KEY | VALUE |
|:---:|:------|
|SYMBOLS| Symbols to be monitored |
|ACCOUNT| Your BTG account number |
|TKNWF| Web Home Broker Token |
|ENDPOINT| Websocket URL |


## AggregatedBookType example
| BID # | BID QTY | BID $ | ASK $ | ASK QTY | ASK # |
|:-----:|:-------:|:-----:|:-----:|:-------:|:-----:|
|   1   |  100.0  | 98.45 |  98.5 |  200.0  |   2   |
|   1   |  3000.0 | 98.43 | 98.54 |  3500.0 |   1   |
|  ...  |   ...   |  ...  |  ...  |   ...   |  ...  |
|   3   |  300.0  | 98.25 |  98.7 |  900.0  |   4   |
|   1   |  100.0  | 98.24 | 98.75 |  400.0  |   4   |


## BusinessBookType example
|  QTY  | PRICE | BUY |          TIME          | SELL | AGRESSOR |
|:-----:|:-----:|:---:|:----------------------:|:----:|:--------:|
|  700  | 22.39 |  40 | Mar 7, 2021 6:11:23 PM |  3   |    I     |
|  1000 | 22.39 |  40 | Mar 7, 2021 6:11:23 PM | 1099 |    I     |
|  ...  |  ...  | ... |         ...            | ...  |   ...    |
|  3000 | 22.39 |  40 | Mar 7, 2021 6:11:23 PM | 386  |    I     |
|  1500 | 22.39 |  40 | Mar 7, 2021 6:11:23 PM | 1099 |    I     |


## AggregatedBookAnalytics

|       ANALYTIC       | RESULT |
|:--------------------:|:------:|
|   Bid/Ask Spread $   | 0.040  |
|      Book depth      |   15   |
|    Book Imbalance    | -0.016 |
|    Balance Ask %     | 0.508  |
|    Weighted Ask $    | 22.736 |
|      Best Ask $      | 22.42  |
|   Weighted Price $   | 22.474 |
| Weighted Mid Price $ | 22.400 |
|    Middle Price $    | 22.400 |
|      Best Bid $      | 22.38  |
|    Weighted Bid $    | 22.209 |
|    Balance Bid %     | 0.492  |

## Broker ranking example
|    BROKER_ID|                     BROKER_NAME|         NET|      QTY|  AGRESSOR|
|:-----------:|:------------------------------:|:----------:|:-------:|:--------:|
|           8 |              UBS Brasil. CCTVM | 18747882.0 | 2765200 |     2301 |
|           3 |     XP INVESTIMENTOS CCTVM S.A |-52130499.0 | 2330000 |     2925 |
|          13 |        MERRILL LYNCH S.A. CTVM |-25250738.0 | 2119500 |      614 |
|         120 |                  BRASIL PLURAL | -1282870.0 | 1462400 |     1454 |
|        1618 |                          IDEAL |  9834157.0 | 1289700 |     1266 |
|          45 | CREDIT SUISSE BRASIL S.A. CTVM | 91518926.0 | 1216700 |     4122 |
|          85 |           BTG PACTUAL CTVM S.A | 41743156.0 | 1074500 |     1004 |
|          40 | MORGAN STANLEY D. W. CTVM S.A. |-32823650.0 |  971200 |      859 |
|          77 |                      CITIGROUP |-55768921.0 |  865100 |      693 |
|          72 |             BRADESCO S.A. CTVM |-10668241.0 |  630900 |      634 |
|         114 |                    ITAU CV S/A |-25425228.0 |  542300 |     1246 |
|         308 |                CLEAR CTVM LTDA |  -121657.0 |  480100 |     1579 |
|         386 |                  OCTO CTVM S/A | -3119380.0 |  384400 |      733 |
|          39 |                AGORA CTVM S.A. | -1111680.0 |  269000 |      256 |
|         238 |   GOLDMAN SACHS DO BRASIL CTVM |  6045594.0 |  191400 |      371 |
|          27 |             SANTANDER S.A. CCT | -4072337.0 |  177200 |      106 |
|         129 |                 PLANNER CV S.A | 15209280.0 |  177100 |      221 |
|          23 |                         NECTON | 10825699.0 |  145800 |      187 |
|          16 |         J. P. MORGAN CCVM S.A. |  -557135.0 |  134100 |      144 |
|        1982 |                     MODAL DTVM |  1203867.0 |  127800 |      380 |



## Widgets for Limit Order Book statistics
![lob widget](img/jupyter_lob_analysis.png)

## Troubleshooting
* update TKNWF token and restart connection
```json
{'message': 'Usuário não autorizado ou token inválido.', 'code': 111}
```


##  Reference

* [Manual](http://files.cedrofinances.com.br/Downloads/Manuais/Manual_Integracao_e_Funcionalidade_WebFeeder.pdf) - Manual de Integração e Funcionalidade
* [Manual BTG Homebroker](https://www.btgpactualdigital.com/content/pdf/BTGPactual_digital_ManualHB.pdf)
* [Paper](http://www.pbcsf.tsinghua.edu.cn/research/caoquanwei/paper/10.The%20Information%20Content%20of%20an%20Open%20Limit%20Order%20Book.pdf) - The information content of an open limit-order book
* [Thesis](https://tspace.library.utoronto.ca/bitstream/1807/70567/3/Rubisov_Anton_201511_MAS_thesis.pdf) - Statistical Arbitrage Using Limit Order Book Imbalance
* [Paper](http://www.columbia.edu/~ww2040/orderbook.pdf) - A stochastic model for order book dynamics
* [Article](https://towardsdatascience.com/four-ways-to-quantify-synchrony-between-time-series-data-b99136c4a9c9) - Four ways to quantify synchrony between time series data
* [SGX-Full-OrderBook-Tick-Data-Trading-Strategy](https://github.com/rorysroes/SGX-Full-OrderBook-Tick-Data-Trading-Strategy) - Modeling High-Frequency Limit Order Book Dynamics Using Machine Learning
*[448Project](https://github.com/HujiaYuYoyo/448Project/blob/master/448_Final.pdf)- High Freq Price Movement Strategy
* [LOB](https://people.maths.ox.ac.uk/porterm/papers/gould-qf-final.pdf)
*[Herd behavior and aggregate fluctuations in financial markets](https://www.researchgate.net/publication/259695552_Herd_behavior_and_aggregate_fluctuations_in_financial_markets)-
