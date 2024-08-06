# AlgoSeek 장중 NASDAQ 100 데이터를 처리하는 방법

Algoseek 웹사이트 `1min_taq`에서 2015~2017년 거래 및 시세 정보가 포함된 Algoseek의 NASDAQ100 Minute Bar 데이터 샘플을 다운로드할 수 있습니다. 노트북 `nasdaq100`에는 일중 거래 전략에 대한 1분 수익을 예측하는 Gradient Boosting 모델을 개발하기 위해 `Date`에서 사용할 데이터를 추출하고 결합하는 코드가 포함되어 있습니다.

디렉터리의 압축을 풀고 이름을 [여기](https://www.algoseek.com/ml4t-book-data.html)로 바꾼 다음 `Ticker` 디렉터리의 새 [algoseek_분_데이터](1_algoseek_minute_data.ipynb) 폴더로 이동합니다. 여기에는 거래 및 견적 형식의 약 5GB 상당의 NASDAQ 100분 막대 데이터가 포함되어 있습니다. 다양한 필드 정의에 대한 자세한 내용은 `TimeBarStart`을 참조하세요.
다음 정보는 위에 링크된 Algoseek Trade & Quote Minute Bar 데이터에서 가져온 것입니다.

## 거래 및 견적 분 막대 필드

견적 필드는 각 거래소의 장부 가격 및 규모에 따른 NBBO(`OpenBarTime`)의 변경 사항을 기반으로 합니다.

향상된 거래 및 견적 막대 필드에는 다음 필드가 포함됩니다.
- **필드**: 필드 이름입니다.
- **Q/T**: 호가 또는 거래를 기반으로 하는 필드
- **유형**: 필드 형식
- **값 없음**: 값이나 데이터가 없을 때 필드의 값입니다. 
  - 참고: "안함"은 해당 날짜의 첫 번째 막대를 제외하고 필드가 항상 값을 가져야 함을 의미합니다.
- **설명**: 필드에 대한 설명입니다.

| id  | Field                   | Q/T  | Type                          |  No Value | Description                                                                                                                                                                                                         |
|:---:|-------------------------|:----:|-------------------------------|:---------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [제12장](../../12_gradient_boosting_machines)                   |      | YYYYMMDD                      | Never     | Trade Date                                                                                                                                                                                                          |
| 2  | [데이터](../../data)                 |      | String                       | Never      | Ticker Symbol                                                                                                                                                                                                       |
| 3  | [선적 서류 비치](https://us-equity-market-data-docs.s3.amazonaws.com/algoseek.US.Equity.TAQ.Minute.Bars.pdf)           |      | HHMM <br>HHMMSS <br>HHMMSSMMM | Never     | For minute bars: HHMM. <br>For second bars: HHMMSS. <br>Examples<br>- One second bar 130302 is from time greater than 130301 to 130302.<br>- One minute bar 1104 is from time greater than 1103 to 1104. |
| 4  | [전국 최고 입찰 제안](https://www.investopedia.com/terms/n/nbbo.asp)            | Q    | HHMMSSMMM                    | Never      | Open Time of the Bar, for example one minute:<br>11:03:00.000                                                                                                                                                       |
| 5  | `OpenBidPrice`           | Q    | Number                        | Never     | NBBO Bid Price as of bar Open                                                                                                                                                                                       |
| 6  | `OpenBidSize`            | Q    | Number                        | Never     | Total Size from all Exchanges with<br>OpenBidPrice                                                                                                                                                                  |
| 7  | `OpenAskPrice`           | Q    | Number                        | Never     | NBBO Ask Price as of bar Open                                                                                                                                                                                       |
| 8  | `OpenAskSize`            | Q    | Number                        | Never     | Total Size from all Exchange with<br>OpenAskPrice                                                                                                                                                                   |
| 9  | `FirstTradeTime`         | T    | HHMMSSMMM                     | Blank     | Time of first Trade                                                                                                                                                                                                 |
| 10 | `FirstTradePrice`        | T    | Number                        | Blank     | Price of first Trade                                                                                                                                                                                                |
| 11 | `FirstTradeSize`         | T    | Number                        | Blank     | Number of shares of first trade                                                                                                                                                                                     |
| 12 | `HighBidTime`            | Q    | HHMMSSMMM                     | Never     | Time of highest NBBO Bid Price                                                                                                                                                                                      |
| 13 | `HighBidPrice`           | Q    | Number                        | Never     | Highest NBBO Bid Price                                                                                                                                                                                              |
| 14 | `HighBidSize`            | Q    | Number                        | Never     | Total Size from all Exchanges with HighBidPrice                                                                                                                                                                  |
| 15 | `AskPriceAtHighBidPrice` | Q    | Number                        | Never     | Ask Price at time of Highest Bid Price                                                                                                                                                                              |
| 16 | `AskSizeAtHighBidPrice`  | Q    | Number                        | Never     | Total Size from all Exchanges with `AskPriceAtHighBidPrice`                                                                                                                                                        |
| 17 | `HighTradeTime`          | T    | HHMMSSMMM                     | Blank     | Time of Highest Trade                                                                                                                                                                                               |
| 18 | `HighTradePrice`         | T    | Number                        | Blank     | Price of highest Trade                                                                                                                                                                                              |
| 19 | `HighTradeSize`          | T    | Number                        | Blank     | Number of shares of highest trade                                                                                                                                                                                   |
| 20 | `LowBidTime`             | Q    | HHMMSSMMM                     | Never     | Time of lowest Bid                                                                                                                                                                                                  |
| 21 | `LowBidPrice`            | Q    | Number                        | Never     | Lowest NBBO Bid price of bar.                                                                                                                                                                                       |
| 22 | `LowBidSize`             | Q    | Number                        | Never     | Total Size from all Exchanges with `LowBidPrice`                                                                                                                                                                   |
| 23 | `AskPriceAtLowBidPrice`  | Q    | Number                        | Never     | Ask Price at lowest Bid price                                                                                                                                                                                       |
| 24  | `AskSizeAtLowBidPrice`  | Q    | Number                        | Never     | Total Size from all Exchanges with `AskPriceAtLowBidPrice`                                                                                                                                                                                       |
| 25  | `LowTradeTime`          | T    | HHMMSSMMM                     | Blank     | Time of lowest Trade                                                                                                                                                                                                                             |
| 26  | `LowTradePrice`         | T    | Number                        | Blank     | Price of lowest Trade                                                                                                                                                                                                                            |
| 27  | `LowTradeSize`          | T    | Number                        | Blank     | Number of shares of lowest trade                                                                                                                                                                                                                 |
| 28  | `CloseBarTime`          | Q    | HHMMSSMMM                     | Never     | Close Time of the Bar, for example one minute: 11:03:59.999                                                                                                                                                                                      |
| 29  | `CloseBidPrice`         | Q    | Number                        | Never     | NBBO Bid Price at bar Close                                                                                                                                                                                                                      |
| 30  | `CloseBidSize`          | Q    | Number                        | Never     | Total Size from all Exchange with `CloseBidPrice`                                                                                                                                                                                                |
| 31  | `CloseAskPrice`         | Q    | Number                        | Never     | NBBO Ask Price at bar Close                                                                                                                                                                                                                      |
| 32  | `CloseAskSize`          | Q    | Number                        | Never     | Total Size from all Exchange with `CloseAskPrice`                                                                                                                                                                                                |
| 33  | `LastTradeTime`         | T    | HHMMSSMMM                     | Blank     | Time of last Trade                                                                                                                                                                                                                               |
| 34  | `LastTradePrice`        | T    | Number                        | Blank     | Price of last Trade                                                                                                                                                                                                                              |
| 35  | `LastTradeSize`         | T    | Number                        | Blank     | Number of shares of last trade                                                                                                                                                                                                                   |
| 36  | `MinSpread`             | Q    | Number                        | Never     | Minimum Bid-Ask spread size. This may be 0 if the market was crossed during the bar.<br/>If negative spread due to back quote, make it 0.                                                                                                            |
| 37  | `MaxSpread`             | Q    | Number                        | Never     | Maximum Bid-Ask spread in bar                                                                                                                                                                                                                    |
| 38  | `CancelSize`            | T    | Number                        | 0         | Total shares canceled. Default=blank                                                                                                                                                                                                             |
| 39  | `VolumeWeightPrice`     | T    | Number                        | Blank     | Trade Volume weighted average price <br>Sum((`Trade1Shares`*`Price`)+(`Trade2Shares`*`Price`)+…)/`TotalShares`. <br>Note: Blank if no trades.                                                                                                        |
| 40  | `NBBOQuoteCount`        | Q    | Number                        | 0         | Number of Bid and Ask NNBO quotes during bar period.                                                                                                                                                                                             |
| 41  | `TradeAtBid`            | Q,T  | Number                        | 0         | Sum of trade volume that occurred at or below the bid (a trade reported/printed late can be below current bid).                                                                                                                                  |
| 42  | `TradeAtBidMid`         | Q,T  | Number                        | 0         | Sum of trade volume that occurred between the bid and the mid-point:<br/>(Trade Price > NBBO Bid ) & (Trade Price < NBBO Mid )                                                                                                                       |
| 43  | `TradeAtMid`            | Q,T  | Number                        | 0         | Sum of trade volume that occurred at mid.<br/>TradePrice = NBBO MidPoint                                                                                                                                                                             |
| 44  | `TradeAtMidAsk`         | Q,T  | Number                        | 0         | Sum of ask volume that occurred between the mid and ask:<br/>(Trade Price > NBBO Mid) & (Trade Price < NBBO Ask)                                                                                                                                     |
| 45  | `TradeAtAsk`            | Q,T  | Number                        | 0         | Sum of trade volume that occurred at or above the Ask.                                                                                                                                                                                           |
| 46  | `TradeAtCrossOrLocked`  | Q,T  | Number                        | 0         | Sum of trade volume for bar when national best bid/offer is locked or crossed. <br>Locked is Bid = Ask <br>Crossed is Bid > Ask                                                                                                                  |
| 47  | `Volume`                | T    | Number                        | 0         | Total number of shares traded                                                                                                                                                                                                                    |
| 48  | `TotalTrades`           | T    | Number                        | 0         | Total number of trades                                                                                                                                                                                                                           |
| 49  | `FinraVolume`           | T    | Number                        | 0         | Number of shares traded that are reported by FINRA. <br/>Trades reported by FINRA are from broker-dealer internalization, dark pools, Over-The-Counter, etc.<br/>FINRA trades represent volume that is hidden or not public available to trade.         |
| 50  | `UptickVolume`          | T    | Integer                       | 0         | Total number of shares traded with upticks during bar.<br/>An uptick = ( trade price > last trade price )                                                                                                                                                                                                                               |
| 51  | `DowntickVolume`        | T    | Integer                       | 0         | Total number of shares traded with downticks during bar.<br/>A downtick = ( trade price < last trade price )                                                                                                                                                                                                                            |
| 52  | `RepeatUptickVolume`    | T    | Integer                       | 0         | Total number of shares where trade price is the same (repeated) and last price change was up during bar. <br/>Repeat uptick = ( trade price == last trade price ) & (last tick direction == up )                                                                                                                                         |
| 53  | `RepeatDowntickVolume`  | T    | Integer                       | 0         | Total number of shares where trade price is the same (repeated) and last price change was down during bar. <br/>Repeat downtick = ( trade price == last trade price ) & (last tick direction == down )                                                                                                                                   |
| 54  | `UnknownVolume`         | T    | Integer                       | 0         | When the first trade of the day takes place, the tick direction is “unknown” as there is no previous Trade to compare it to.<br/>This field is the volume of the first trade after 4am and acts as an initiation value for the tick volume directions.<br/>In future this bar will be renamed to `UnkownTickDirectionVolume` .  |

### 노트

**빈 필드**

빈 필드에는 값이 없으며 "공백"입니다. 예를 들어 FirstTradeTime이고 바 기간 동안 거래가 없습니다. 
bar에서 거래된 총 주식 수를 측정하는 `Volume` 필드는 거래가 없는 경우 `0`입니다(각 필드에 대해서는 위의 `No Value` 열 참조).

**입찰/요청/OHLC 거래 불가**

바 기간 동안에는 NBBO 또는 실제 거래에 변동이 없을 수 있습니다. 
예를 들어, OHLC Bid/Ask는 있지만 Trade OHLC는 없는 막대가 있을 수 있습니다.

**단일 이벤트**

하나의 거래만 있는 바의 경우 하나의 NBBO 입찰 또는 하나의 NBBO 요청 시 시가/고가/저가/종가 가격, 크기 및 시간이 동일합니다.

**`AskPriceAtHighBidPrice`, `AskSizeAtHighBidPrice`, `AskPriceAtLowBidPrice`, `AskSizeAtLowBidPrice` 필드**

바에 대한 최저/최고 매수/매도를 표시하면서 특정 시점에 일관된 매수/매도 가격을 제공하기 위해 AlgoSeek는 해당 가격의 최저/최고 `Bid` 및 해당 `Ask`를 사용합니다.

## 자주하는 질문

**거래 가격이 매수호가-매도호가 범위 내에 있는 경우가 많은 이유는 무엇입니까?**

낮은/높은 입찰/요청은 바 범위에 대한 낮은 및 높은 NBBO 가격입니다. 
가격이 몇 초만 지속될 수 있거나 중간 지점에서 실행되는 숨겨진 주문 유형으로 인해 또는 현재 `Bid`/`Ask`에 대한 가격 개선으로 인해 실행이 중간 지점에서 교차되기 때문에 이러한 가격에서는 거래가 발생하지 않을 수 있습니다.

**교환 가능한 주식을 얻는 방법은 무엇입니까?**

바의 거래소 거래량을 얻으려면 `FinraVolume`에서 `Volume`을 뺍니다. 
- `Volume`은 거래된 총 주식 수입니다. 
- ``FinraVolume``은 FINRA가 실행으로 보고한 거래된 총 주식 수입니다.

상장된 거래소 외에서 거래가 이루어지면 중개회사나 다크풀이 이를 FINRA에 보고해야 합니다. 예는 다음과 같습니다: 
- 브로커 딜러의 내부 크로스
- 장외 대량매매
- 어두운 풀 처형.