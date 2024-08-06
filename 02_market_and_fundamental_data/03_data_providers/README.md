# 02 시장 데이터에 대한 API 접근

Python을 사용하여 API를 통해 시장 데이터에 액세스하는 몇 가지 옵션이 있습니다.

## 팬더 데이터리더

`pandas` 노트북은 Pandas 라이브러리에 내장된 몇 가지 소스를 제공합니다. 
- [01_pandas_datareader_demo](01_pandas_datareader_demo.ipynb) 라이브러리를 사용하면 read_html 함수를 사용하여 웹사이트에 표시된 데이터에 액세스할 수 있습니다. 
- 관련 `pandas-datareader` 라이브러리는 표준 인터페이스를 통해 다양한 데이터 공급자의 API 엔드포인트에 대한 액세스를 제공합니다.

## yfinance: 야후! 금융시장 및 기초자료

[yfinance_demo](02_yfinance_demo.ipynb) 노트북은 yfinance를 사용하여 Yahoo!에서 다양한 데이터를 다운로드하는 방법을 보여줍니다. 재원. 라이브러리는 Pythonic API를 사용하여 안정적이고 효율적인 방식으로 웹 사이트에서 데이터를 스크랩하여 기록 데이터 API의 지원 중단을 해결합니다.

## 랍스터 틱 데이터

`zipline` 노트북은 사용하기 쉽고 고품질의 지정가 주문장 데이터를 제공하는 것을 목표로 하는 [온라인](https://lobsterdata.com/info/WhatIsLOBSTER.php) 지정가 주문장 데이터 도구인 LOBSTER(한도 주문장 시스템 - 효율적인 재구성자)에서 제공하는 주문장 데이터의 사용을 보여줍니다.

2013년부터 LOBSTER는 학계의 데이터 제공자 역할을 하여 나스닥 거래 주식의 전체 세계에 대해 재구성된 지정가 주문장 데이터에 대한 액세스를 제공합니다. 최근에는 상용 서비스를 제공하기 시작했습니다.

## 퀀들

[03_quandl_demo](03_quandl_demo.ipynb) 노트북은 Quandl이 매우 간단한 API를 사용하여 무료 및 프리미엄 데이터를 제공하는 방법을 보여줍니다. 자세한 내용은 [선적 서류 비치](https://www.quandl.com/tools/api)을 참조하세요.

## 짚라인과 콴토피안

노트북 [노트북 [zipline_data]가 포함되어 있습니다.](05_zipline_data.ipynb)은 이 책 전체에서 사용할 백테스팅 라이브러리 [03_랍스터_가치_데이터](03_lobster_itch_data.ipynb)를 간략하게 소개하고 백테스트를 실행하는 동안 주가 데이터에 액세스하는 방법을 보여줍니다. 설치에 대해서는 [여기](../../installation) 지침을 참조하세요.

