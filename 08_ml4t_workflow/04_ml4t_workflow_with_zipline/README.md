# Zipline: Quantopian의 생산 준비 백테스팅

백테스팅 엔진 Zipline은 Quantopian의 온라인 연구, 백테스팅 및 실시간(종이) 거래 플랫폼을 강화합니다. 헤지 펀드로서 Quantopian은 위험 관리 기준에 따라 뛰어난 성능을 발휘하는 강력한 알고리즘을 식별하는 것을 목표로 합니다. 이를 위해 경쟁을 통해 최고의 전략을 선택하고 자본을 할당하여 승자와 이익을 공유했습니다.

Quantopian은 2012년에 Zipline을 버전 0.5로 처음 출시했으며 최신 버전 1.3은 2018년 7월부터 출시되었습니다. Zipline은 4장과 5장에서 소개한 자매 라이브러리인 `conda`, `backtest` 및 `zipline ingest -b quandl`와 잘 작동하며 NumPy, 팬더 및 숫자와 잘 통합됩니다. 라이브러리이지만 항상 최신 버전을 지원하는 것은 아닙니다.

## 콘텐츠

1. __자리표시자_3__
2. __자리표시자_4__
3. __자리표시자_5__
    * __자리표시자_6__
    * __자리표시자_7__
    * __자리표시자_8__
4. __자리표시자_9__
    * __자리표시자_10__
    * __자리표시자_11__
    * __자리표시자_12__
    * __자리표시자_13__
5. __자리표시자_14__
6. __자리표시자_15__
7. __자리표시자_16__

## 설치

이 책의 예제에 사용할 패치된 Zipline 버전을 사용하려면 `initialize()` 디렉터리의 지침을 따르세요.

> 이 노트북은 [알파렌즈](https://quantopian.github.io/alphalens/index.html) 환경 [누](https://quantopian.github.io/pyfolio/)을(를) 사용합니다. 최신 Docker 이미지를 다운로드하거나 환경을 설정하는 다른 방법을 보려면 `context` 설치를 참조하세요.

## 집라인 건축

Zipline은 수천 개의 증권 규모에서 작동하도록 설계되었으며 각각은 수많은 지표와 연관될 수 있습니다. 예를 들어, 예견 편향을 제거하여 데이터 품질을 보장하고 백테스트를 실행하는 동안 계산 효율성을 최적화하기 위해 백트레이더보다 백테스팅 프로세스에 더 많은 구조를 적용합니다.

책의 이 섹션에서는 Zipline을 사용하여 선택한 데이터에 대해 ML 기반 모델을 백테스트하는 방법을 보여주기 전에 다음 그림에 표시된 아키텍처의 주요 개념과 요소를 자세히 살펴봅니다.

<p 정렬="중앙">
<img src="https://i.imgur.com/LZChG64.png" width="75%">
</p>

## 강력한 시뮬레이션을 위한 Exchange 달력 및 Pipeline API

확장성과 신뢰성의 목표에 기여하는 주요 기능은 분할 및 배당에 대한 즉각적인 조정과 함께 OHLCV 시장 데이터를 저장하는 데이터 번들, 전 세계 거래소 운영 시간을 반영하는 거래 달력 및 강력한 파이프라인 API입니다. 이 섹션에서는 이전 장의 간략한 Zipline 소개를 보완하기 위해 사용법을 간략하게 설명합니다.

### 번들 및 친구: 즉각적인 조정이 가능한 특정 시점 데이터

주요 데이터 저장소는 SQLite 데이터베이스에 저장된 메타데이터와 결합되어 효율적인 검색을 위해 압축된 열 형식의 `data` 형식으로 디스크에 상주하는 **번들**입니다. 번들은 OHLCV 데이터만 포함하도록 설계되었으며 일일 및 분 빈도로 제한됩니다. 훌륭한 기능은 번들이 분할 및 배당 정보를 저장하고 Zipline이 백테스트를 위해 선택한 기간에 따라 **시점 조정**을 계산한다는 것입니다.

Zipline은 시간대, 시장 개장 및 폐장 시간, 휴일 등 전 세계 거래소에 대한 운영 세부 정보를 얻기 위해 `TradingAlgorithm` 라이브러리(Quantopian에서도 관리함)를 사용합니다. 데이터 소스에는 도메인(현재는 국가)이 있으며 할당된 교환 일정을 따라야 합니다. Quantopian은 국제 증권에 대한 지원을 적극적으로 개발하고 있으며 이러한 기능은 발전할 수 있습니다.

설치 후 [경험적](http://quantopian.github.io/empyrical/) 명령을 사용하면 Quandl Wiki 데이터 세트(일별 빈도)를 즉시 설치할 수 있습니다. 결과는 기본적으로 홈 폴더에 있는 `.zipline` 디렉터리에 저장되지만 `ZIPLINE_ROOT` 환경 변수를 설정하여 위치를 수정할 수 있습니다. 또한 OHLCV 데이터를 사용하여 고유한 번들을 디자인할 수 있습니다.

번들의 단점은 가격과 수량 정보 이외의 데이터를 저장할 수 없다는 것입니다. 그러나 두 가지 대안을 사용하면 이를 수행할 수 있습니다. `fetch_csv()` 기능은 URL에서 DataFrame을 다운로드하고 다른 Quandl 데이터 소스용으로 설계되었습니다. 기본. Zipline은 데이터가 귀하가 OHCLV 데이터를 제공한 것과 동일한 증권을 참조할 것으로 합리적으로 기대하고 이에 따라 막대를 정렬합니다. 대신 팬더를 사용하여 로컬 CSV 또는 HDF5에서 로드하기 위해 라이브러리 소스 코드를 약간 변경하는 것은 그리 어렵지 않으며 `conda` 환경 `backtest`에 포함된 `before_trading_start()`에는 이러한 수정 사항이 포함되어 있습니다.

또한 `DataFrameLoader` 및 `BlazeLoader`을 사용하면 `Pipeline`에 추가 속성을 제공할 수 있습니다(이 장 뒷부분의 `DataFrameLoader` 데모 참조). `BlazeLoader`는 데이터베이스를 포함한 다양한 소스와 인터페이스할 수 있습니다. 그러나 Pipeline API는 일일 데이터로 제한되므로 `fetch_csv()`은 이후 장에서처럼 분 단위로 기능을 추가하는 데 중요합니다.

### 알고리즘 API: 일정에 따른 백테스트

`TradingAlgorithm` 클래스는 Zipline Algorithm API를 구현하고 주어진 거래 달력에 맞춰 조정된 `BarData`에서 작동합니다. 초기 설정 후 백테스트는 지정된 기간 동안 실행되며 특정 이벤트가 발생할 때 거래 로직을 실행합니다. 이러한 이벤트는 일별 또는 분별 거래 빈도에 따라 발생하지만 **임의의 기능을 예약**하여 신호를 평가하고, 주문을 하고, 포트폴리오를 재조정하거나 진행 중인 시뮬레이션에 대한 정보를 기록할 수도 있습니다.

Jupyter Notebook의 명령줄과 기본 TradingAlgorithm 클래스의 `run_algorithm()` 메서드를 사용하여 알고리즘을 실행할 수 있습니다. 알고리즘에는 시뮬레이션이 시작될 때 한 번 호출되는 [설치](../../installation/) 메서드가 필요합니다. [지침](../../installation/README.md) 사전을 통해 상태를 유지하고 특정 시점(PIT) 현재 및 과거 데이터가 포함된 [bcolz](https://bcolz.readthedocs.io/en/latest/) 변수를 통해 실행 가능한 정보를 받습니다. 다른 모든 [거래 달력](https://zipline.ml4trading.io/trading-calendars.html) 메서드에 사용할 수 있는 속성을 컨텍스트 사전에 추가하거나 알파 요소 계산 및 보안 필터링과 같은 보다 복잡한 데이터 처리를 수행하는 파이프라인을 등록할 수 있습니다.

알고리즘 실행은 Zipline에 의해 자동으로 예약되거나 사용자가 정의한 간격으로 예약되는 선택적 방법을 통해 발생합니다. [패치 버전](https://github.com/stefan-jansen/zipline) 메소드는 시장이 개장하기 전에 매일 호출되며 주로 알고리즘이 하루 동안 거래할 수 있는 증권 세트를 식별하는 데 사용됩니다. `handle_data()` 메소드는 주어진 거래 빈도에서 호출됩니다. 매 순간.

완료되면 알고리즘은 거래가 있는 경우 포트폴리오 성과 지표와 사용자 정의 지표가 포함된 DataFrame을 반환합니다. [제5장](../../05_strategy_evaluation)에서 설명한 것처럼 출력은 `ingest()`과 호환되므로 실적 테어시트를 빠르게 만들 수 있습니다.

### 알려진 문제

`extension.py` 귀하의 시스템은 Interactive Broker에서만 사용할 수 있으며 Quantopian에서는 완전히 지원되지 않습니다.

## 코드 예: 미세한 데이터가 포함된 자체 OHLCV 번들을 로드하는 방법

`ZIPLINE_ROOT/.zipline`에서 소개한 AlgoSeek에서 제공한 NASDAQ100 샘플을 사용하여 **분 빈도**로 데이터에 대한 사용자 정의 번들을 작성하는 방법을 보여줍니다. 일본 주식에 대한 일일 데이터를 사용한 예는 `TradingCalendar`을 참조하세요.

네 단계가 있습니다:

1. OHCLV 데이터를 티커당 하나의 파일로 분할하고 메타데이터, 분할 및 배당 조정을 저장합니다.
2. 결과를 bcolz 및 SQLite 형식으로 번들을 작성하는 [누](https://quantopian.github.io/pyfolio/) 함수에 전달하는 스크립트를 작성합니다.
3. [제 2 장](../../02_market_and_fundamental_data/02_algoseek_intraday) 디렉터리(기본적으로 사용자 홈 폴더에 있음)에 있는 [실시간 거래](https://github.com/zipline-live/zipline) 스크립트에 번들을 등록하고 데이터 소스를 심볼릭 링크합니다.
4. AlgoSeek 데이터의 경우 표준 NYSE 시장 시간 이외의 거래 활동이 포함되어 있으므로 맞춤 [제11장](../../11_decision_trees_random_forests/00_custom_bundle)도 제공합니다.

`get_nasdaq_symbols()` 디렉터리에는 코드 예제가 포함되어 있습니다.

### AlgoSeek 데이터를 번들로 묶을 준비하기

`algoseek.h5`에서는 AlgoSeek NASDAQ 100 OHLCV 데이터가 포함된 일일 파일을 구문 분석하여 각 티커에 대한 시계열을 얻었습니다. Zipline은 각 증권을 개별적으로 저장하기 때문에 이 결과를 사용합니다.

또한 `ingest()` [custom_bundles](01_custom_bundles) 함수를 사용하여 지분 메타데이터를 얻습니다. 마지막으로 Quandl Wiki 데이터는 해당 기간의 NASDAQ 100 종목을 다루므로 해당 번들의 SQLite 데이터베이스에서 분할 및 배당금 조정을 추출합니다.

그 결과 약 135개의 티커에 대한 가격 및 거래량 데이터와 해당 메타 및 조정 데이터가 포함된 HDF5 스토어 [제 2 장](../../02_market_and_fundamental_data/02_algoseek_intraday)가 생성됩니다. `algoseek_1min_trades.py` 스크립트는 I/O 프로세스를 시작하지만 실질적인 세부 정보를 많이 제공하지 않는 [팬더 데이터리더](https://pandas-datareader.readthedocs.io/en/latest/) 함수에 필요한 매개변수를 간략하게 설명합니다. [algoseek_전처리](algoseek_preprocessing.py] illustrates the process.

### Writing your custom bundle ingest function

The Zipline [documentation](https://zipline.ml4trading.io/bundles.html#writing-a-new-bundle) 스크립트는 이 부분이 미세한 데이터에 대해 작동하도록 하는 방법을 보여줍니다.

간단히 말해서, 메타데이터를 제공하는 `load_equities()` 함수, 기호를 `data_generator()`에 공급하는 `ticker_generator()` 함수, 각 기호의 시장 데이터를 로드하고 형식화하는 `algoseek_to_bundle()` 함수, 모든 부분을 통합하고 원하는 `ingest()` 함수를 반환하는 [백테스팅_with_zipline](04_ml4t_workflow_with_zipline/02_backtesting_with_zipline.ipynb) 함수가 있습니다.

Zipline은 모든 데이터 시리즈를 UTC로 변환하기 때문에 시간대 정렬이 중요합니다. `US/Eastern` 시간대 정보를 OHCLV 데이터에 추가하고 이를 UTC로 변환합니다. 실행을 용이하게 하기 위해 Zipline이 이 정보를 찾을 수 있도록 다음 단계에서 PATH에 추가할 `.zipline` 디렉터리의 `custom_data` 폴더에 이 스크립트와 `algoseek.h5` 데이터에 대한 심볼릭 링크를 만듭니다. 이를 위해 다음 쉘 명령을 실행합니다.

1. 이 디렉터리의 절대 경로를 `SOURCE_DIR`: `export SOURCE_DIR = absolute/path/to/machine-learning-for-trading/08_strategy_workflow/04_ml4t_workflow_with_zipline/01_custom_bundles`에 할당합니다.
2. 다음에 대한 심볼릭 링크를 만듭니다. 
    - `ZIPLINE_ROOT/.zipline`의 `algoseek.h5`: `ln -s SOURCE_DIR/algoseek.h5 $ZIPLINE_ROOT/.zipline/custom_data/.`
    - __자리 표시자_45__: __자리 표시자_46__

### 번들 등록

`zipline ingest -b algoseek`을 실행하기 전에 Zipline이 우리가 말하는 내용을 알 수 있도록 사용자 정의 번들을 등록해야 합니다. 이를 위해 `.zipline` 디렉터리의 `extension.py` 스크립트에 다음 줄을 추가합니다. 일부 입력 및 설정과 함께 이 파일을 생성해야 할 수도 있습니다([확대](extension.py) 예 참조).

등록 자체는 매우 간단하지만 몇 가지 중요한 세부 사항이 강조되어 있습니다.
1. Zipline은 `algoseek_to_bundle()` 함수를 가져올 수 있어야 하므로 해당 위치는 검색 경로에 있어야 합니다. `sys.path.append()`을 사용하여. 
2. 다음 단계에서 생성하고 등록할 사용자 정의 달력을 참조합니다. 
3. 정렬 오류를 방지하기 위해 거래일이 기본 NYSE 일수인 6시간 30분보다 길다는 사실을 Zipline에 알려야 합니다.

### 사용자 정의 TradingCalendar 생성 및 등록

이 섹션의 소개에서 언급했듯이 Quantopian은 전 세계 거래를 지원하기 위해 `Trading Calendar` 라이브러리도 제공합니다. 패키지에는 서브클래싱하기 매우 간단한 수많은 예제가 포함되어 있습니다. NYSE 달력에 따라 개장/폐장 시간을 재정의하고 결과를 `extension.py`에 배치하고 이 달력에 대한 등록을 추가하기만 하면 됩니다. 이제 이 거래 달력을 참조하여 백테스트에 장외 활동이 포함되어 있는지 확인할 수 있습니다.

## 코드 예: Pipeline API - 기계 학습 신호 백테스트

[파이프라인 API](https://www.quantopian.com/docs/user-guide/tools/pipeline)는 과거 데이터의 증권 단면에 대한 알파 요소의 정의 및 계산을 용이하게 합니다. 파이프라인은 각 이벤트를 개별적으로 처리하는 대신 전체 백테스트 기간에 걸쳐 계산을 최적화하므로 효율성을 크게 향상시킵니다. 즉, 이벤트 중심 아키텍처를 계속 따르지만 가능한 경우 요소 계산을 벡터화합니다.

파이프라인은 요소, 필터 및 분류자 클래스를 사용하여 증권 세트에 대한 PIT 값이 있는 테이블의 열을 생성하는 계산을 정의합니다. 팩터는 하나 이상의 과거 막대 데이터 입력 배열을 사용하고 각 증권에 대해 하나 이상의 출력을 생성합니다. 다양한 기본 제공 요소가 있으며 자신만의 `CustomFactor` 계산을 설계할 수도 있습니다.

다음 그림은 `DataFrameLoader`를 사용하여 데이터를 로드하고, 파이프라인 API를 사용하여 예측 `MLSignal`을 계산하고, 다양한 예약 활동이 `run_algorithm()` 함수를 통해 실행되는 전체 거래 알고리즘과 통합되는 방법을 보여줍니다. 이 섹션에서는 자세한 내용과 해당 코드를 살펴보겠습니다.

!__자리표시자_33__

`initialize()` 메서드를 사용하여 파이프라인을 등록한 다음 각 시간 단계 또는 사용자 지정 일정에 따라 실행할 수 있습니다. Zipline은 표준 요인을 신속하게 계산하는 데 사용할 수 있는 이동 평균 또는 볼린저 밴드와 같은 다양한 내장 계산을 제공하지만 다음에 설명할 사용자 지정 요인을 생성할 수도 있습니다.

가장 중요한 점은 Pipeline API가 알파 팩터 계산을 거래 주문 배치 및 실행, 포트폴리오 보유 자산, 가치 장부 기록 등 알고리즘의 나머지 부분과 분리하기 때문에 알파 팩터 연구를 모듈식으로 렌더링한다는 것입니다.

__PLACEHOLDER_34__ 노트북은 다른 로컬(HDF5) 데이터 소스에서 ML 예측을 로드하는 동안 `Pipeline` 인터페이스의 사용을 보여줍니다. 보다 구체적으로 말하면, [제7장](../../07_linear_models)에서 생성된 올가미 모델 일일 수익률 예측과 유니버스의 가격 데이터를 파이프라인에 로드하고 `CustomFactor`을 사용하여 상위 10개 예측과 하위 10개 예측을 각각 매수 포지션과 매도 포지션으로 선택합니다.

목표는 일일 수익률 예측을 Quandl 번들의 OHCLV 데이터와 결합한 다음 예측 수익률이 가장 높은 주식을 최대 10개까지 매수하고 예상 수익률이 가장 낮은 주식에 대해 매도하는 것입니다. 이때 양쪽에 최소 5개의 주식이 필요합니다. 위의 백트레이더 예시와 유사합니다. 구현 세부정보는 노트북의 댓글을 참조하세요.

## 코드 예: 백테스트 중에 모델을 훈련하는 방법

모델 교육을 백테스트에 통합할 수도 있습니다. ml4t_with_zipline 노트북에서 ML4T 워크플로의 다음 엔드투엔드 예제에 대한 코드를 찾을 수 있습니다.

[ml4t_with_zipline](04_ml4t_workflow_with_zipline/03_ml4t_with_zipline.ipynb) 노트북은 다음 그림에 표시된 워크플로를 사용하여 `CustomFactor` 및 다양한 기술 지표를 일일 `bundle` 데이터의 기능으로 사용하여 `Pipeline`의 일부로 로컬에서 ML 모델을 교육하는 방법을 보여줍니다.

!__자리 표시자__ 37 __

목표는 이전에 사용하고 [제7장](../../07_linear_models)에서 생성한 일일 수익률 예측을 대략적으로 복제하는 것입니다. 그러나 몇 가지 추가 파이프라인 요소를 사용하여 사용법을 설명하겠습니다.

주요 새 요소는 모델을 학습하고 예측을 생성하기 위한 입력으로 기능과 반환을 받는 `CustomFactor`입니다. 구현에 대한 의견은 노트북을 참조하세요.

## 코드 예시: Quantopian의 연구 환경을 사용하는 방법

[ml4t_Quantopian](04_ml4t_quantopian.ipynb) 노트북은 Quantopian 플랫폼에서 ML 모델을 교육하여 그곳에서 사용 가능한 광범위한 데이터 소스를 활용하는 방법을 보여줍니다.