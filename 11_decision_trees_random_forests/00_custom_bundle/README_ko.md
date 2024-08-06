# STOOQ에서 공급되는 일본 주식용 맞춤형 번들

일본 주식 데이터를 사용하여 `Zipline`에 대한 [맞춤 번들](https://zipline.ml4trading.io/bundles.html#writing-a-new-bundle)을(를) 생성하겠습니다. 먼저 `Zipline`을 참조하세요.

우리는 다음과 같은 조치를 취할 것입니다:
1. 시세, 가격 및 조정에 대한 정보가 포함된 여러 데이터 파일을 만듭니다.
2. 데이터 처리 및 저장을 처리하는 [다운로드 지침](../../data/create_stooq_data.ipynb) 수집 함수를 코딩합니다.
3. 새로운 `bundle`을 등록하는 `Zipline` 확장을 정의합니다.
4. `Zipline ingest` 명령이 해당 파일을 찾을 수 있도록 `Zipline_ROOT` 디렉터리에 파일을 배치합니다.

## 설정

`Zipline`을(를) 사용하면 시가, 고가, 저가, 종가 및 거래량(OHCLV) 정보는 물론 주식 분할 및 배당금 지급과 같은 조정 사항이 포함된 맞춤형 번들을 생성할 수 있습니다.

기본적으로 사용자 홈 디렉터리인 `~/.Zipline`의 `.Zipline` 디렉터리에 데이터를 저장합니다. 하지만 이 책에서 제공하는 도커 이미지와 마찬가지로 `Zipline_ROOT` 환경 변수를 설정하여 대상 위치를 수정할 수 있습니다.

## 데이터 전처리

데이터를 준비하기 위해 HDF5 형식으로 세 가지 종류의 데이터 테이블을 만듭니다.
1. `equities`: 보안을 위한 고유한 `sid`, `ticker` 및 `name`을 포함합니다.
2. `jp.<sid>`라는 이름의 ~2,900개 자산 각각에 대한 OHLCV 데이터가 포함된 가격표
3. `splits`: 분할 요소를 포함하며 필수입니다. 데이터가 이미 조정되었으므로 한 줄에 1.0의 계수를 사용하여 한 줄만 추가하면 됩니다.

`stooq_preprocessing` 파일은 이러한 단계를 구현하고 HDF5 파일 `stooq.h5`에 테이블을 생성합니다.

## `Zipline` 수집 기능

`stooq_jp_stocks.py` 파일은 사용자 정의 번들을 생성하기 위해 `Zipline`에 필요한 `ingest` 함수를 반환하는 `stooq_jp_to_bundle(interval='1d')` 함수를 정의합니다([문서](https://zipline.ml4trading.io/bundles.html#writing-a-new-bundle) 참조. 다음 서명이 필요합니다:

__자리표시자_0__

이 함수는 `ingest` 프로세스 중 이전 단계에서 생성한 정보를 로드합니다. 필요에 따라 `(sid, ticker)` 튜플을 로드하고 해당 OHLCV 정보를 올바른 형식으로 생성하는 `data_generator()`로 구성됩니다. 또한 Zipline이 올바른 달력과 거래 날짜 범위를 연결할 수 있도록 거래소에 대한 정보를 추가합니다.

또한 이 경우 활성 역할을 수행하지 않는 조정 데이터를 로드합니다.

## 번들 등록

Zipline은 번들이 존재하는지와 방금 정의한 `ingest` 함수를 생성하는 방법을 알아야 합니다. 이를 위해 번들 이름을 전달하고 `ingest` 함수(즉, `stooq_jp_stocks.py`의 `stooq_jp_to_bundle()`)를 반환하는 함수를 찾고 사용할 거래 달력(도쿄 거래소의 경우 `XTKS`)을 나타내는 `extension.py` 파일을 생성합니다.

## 파일 위치

마지막으로 Zipline이 파일을 찾을 수 있도록 이러한 파일을 올바른 위치에 배치해야 합니다. 이 디렉토리에 실제 파일을 유지하면서 기호 링크를 사용할 수 있습니다.

보다 구체적으로 다음과 같은 심볼릭 링크를 만들겠습니다. 
1. ZIPLINE_ROOT 디렉토리의 `stooq_jp_stocks.py`에, 그리고 
2. `ZIPLINE_ROOT/custom_data`의 stooq.h5에

Linux 또는 MacOSX에서 이는 셸을 열고 다음 명령을 실행하는 것을 의미합니다. 여기서 PROJECT_DIR은 컴퓨터에 있는 이 저장소의 루트 폴더에 대한 절대 경로를 나타냅니다.
__자리표시자_1__

결과적으로 디렉터리 구조는 다음과 같아야 합니다(이러한 파일 중 일부는 기호 링크임).
__자리표시자_2__

