# 재무 특성 엔지니어링: 알파 요소를 조사하는 방법

알고리즘 거래 전략은 지수와 같은 벤치마크에 비해 우수한 수익을 창출하기 위해 자산을 사고 팔 때를 나타내는 신호에 의해 주도됩니다. 이 벤치마크에 대한 노출로 설명되지 않는 자산 수익의 부분을 알파라고 하며, 따라서 상관관계가 없는 수익을 생성하는 것을 목표로 하는 신호를 알파 팩터라고도 합니다.

ML에 이미 익숙하다면 특성 추출이 성공적인 예측을 위한 핵심 요소라는 것을 알 수 있습니다. 이는 거래에서도 다르지 않습니다. 그러나 투자는 시장이 어떻게 작동하는지, 그리고 결과적으로 가격 변동을 설명하거나 예측하기 위해 다른 기능보다 더 잘 작동할 수 있는 기능에 대한 수십 년 간의 연구를 통해 특히 풍부합니다. 이 장에서는 알파 요인을 검색하기 위한 시작점으로 개요를 제공합니다.

이 장에서는 또한 알파 요소 계산 및 테스트를 용이하게 하는 주요 도구를 제공합니다. NumPy, pandas 및 TA-Lib 라이브러리가 어떻게 데이터 조작을 용이하게 하는지 강조하고 데이터의 노이즈를 줄이는 데 도움이 되는 웨이블릿 및 Kalman 필터와 같은 널리 사용되는 평활화 기술을 제시합니다.

또한 거래 시뮬레이터 Zipline을 사용하여 (전통적인) 알파 팩터의 예측 성능을 평가하는 방법도 미리 살펴봅니다. 정보 계수 및 요인 회전율과 같은 주요 알파 요인 측정 항목에 대해 논의합니다. 기계 학습을 사용하는 백테스팅 거래 전략에 대한 심층적인 소개는 `PyKalman`에서 이어지며, 이 책 전체에서 거래 전략을 평가하는 데 사용할 **ML4T 워크플로**를 다룹니다.

광범위한 알파 요소를 계산하는 수많은 코드 예제를 포함하여 이 주제에 대한 추가 자료를 보려면 `PyWavelets`을 참조하세요.

## 콘텐츠

1. __자리표시자_2__
2. __자리표시자_3__
    * __자리표시자_4__
3. __자리표시자_5__
    * __자리표시자_6__
    * __자리표시자_7__
    * __자리표시자_8__
    * __자리표시자_9__
    * __자리표시자_10__
4. __자리표시자_11__
    * __자리표시자_12__
    * __자리표시자_13__
    * __자리표시자_14__
5. __자리표시자_15__

## 실제 알파 팩터: 데이터에서 신호까지

알파 팩터는 예측 신호가 포함된 시장, 기본 및 대체 데이터의 변형입니다. 이는 자산 수익률을 높이는 위험을 포착하도록 설계되었습니다. 한 세트의 요인은 성장, 인플레이션, 변동성, 생산성 및 인구통계학적 위험과 같은 경제 전반의 기본 변수를 설명합니다. 또 다른 세트는 시장 포트폴리오, 가치 성장 투자, 모멘텀 투자와 같은 거래 가능한 투자 스타일로 구성됩니다.

경제학이나 금융 시장의 제도적 설정, 투자자 행동(이러한 행동에 대한 알려진 편견 포함)을 기반으로 가격 변동을 설명하는 요소도 있습니다. 팩터 뒤에 있는 경제 이론은 합리적일 수 있습니다. 여기서 팩터는 불경기 동안 낮은 수익을 보상하기 위해 장기적으로 높은 수익을 얻습니다. 또는 행동적(팩터 리스크 프리미엄은 에이전트의 편향되거나 완전히 합리적이지 않은 행동에서 발생함)일 수 있습니다. 중재되지 않습니다.

## 수십 년간의 요인 연구를 기반으로 구축

이상적인 세계에서 위험 요인의 범주는 서로 독립적(직교)이어야 하고, 양의 위험 프리미엄을 산출해야 하며, 위험의 모든 차원을 포괄하고 특정 클래스의 자산에 대한 체계적인 위험을 설명하는 완전한 세트를 형성해야 합니다. 실제로 이러한 요구 사항은 대략적으로만 유지됩니다.

### 참고자료

- Eugene Fama와 Ken French의 [이상 징후 분석](http://schwert.ssb.rochester.edu/f532/ff_JF08.pdf)(2008)
- [주식 수익률 설명: 문헌 검토](https://www.ifa.com/pdfs/explainingstockreturns.pdf) 제임스 L. 데이비스(2001)
- [시장 효율성, 장기 수익 및 행동 금융](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=15108) 작성자: Eugene Fama(1997)
- 버튼 말키엘의 [효율적 시장 가설과 비판](https://pubs.aeaweb.org/doi/pdf/10.1257/089533003321164958)(2003)
- [새로운 팔그레이브 경제학 사전](https://www.palgrave.com/us/book/9780333786765)(2008) Steven Durlauf 및 Lawrence Blume 저, 2판.
- [이상현상과 시장 효율성](https://www.nber.org/papers/w9277.pdf) 작성자: G. William Schwert25("금융 경제학" 핸드북의 Ch. 15, 작성자: Constantinides, Harris 및 Stulz, 2003)
- [투자자 심리 및 자산 가격](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=265132), 작성자: David Hirshleifer(2001)
- [크고 복잡한 데이터 세트 분석을 위한 실용적인 조언](https://www.unofficialgoogledatascience.com/2016/10/practical-advice-for-analysis-of-large.html), Patrick Riley, 비공식 Google 데이터 과학 블로그

## 수익을 예측하는 엔지니어링 알파 팩터

핵심 요소 범주, 그 근거 및 대중적인 지표에 대한 개념적 이해를 바탕으로 핵심 작업은 이전에 제시된 수익 동인에 의해 구체화된 위험을 더 잘 포착할 수 있는 새로운 요소를 식별하거나 새로운 요소를 찾는 것입니다. 두 경우 모두 혁신적인 요소의 성능을 알려진 요소의 성능과 비교하여 증분 신호 이득을 식별하는 것이 중요합니다.

### 코드 예: Pandas 및 NumPy를 사용하여 요소를 엔지니어링하는 방법

[데이터](00_data) 디렉터리의 노트북 [feature_engineering.ipynb](00_data/feature_engineering.ipynb)은 기본 요소를 엔지니어링하는 방법을 보여줍니다.

### 코드 예: TA-Lib를 사용하여 기술 알파 팩터를 생성하는 방법

[How_to_use_talib](02_how_to_use_talib.ipynb) 노트북은 광범위한 공통 기술 지표를 포함하는 TA-Lib의 사용법을 보여줍니다. 이들 지표는 가격, 거래량 정보 등 시장 데이터만 활용한다는 공통점이 있다.

**부록**의 노트북 __PLACEHOLDER__ 27 __에는 수십 개의 추가 예제가 포함되어 있습니다.

### 코드 예: 칼만 필터를 사용하여 알파 요소의 잡음을 제거하는 방법

노트북 [kalman_filter_and_wavelets](03_kalman_filter_and_wavelets.ipynb)은 평활화를 위해 [제6장](../08_ml4t_workflow) 패키지를 사용하는 Kalman 필터의 사용을 보여줍니다. 또한 쌍 거래 전략을 개발할 때 [제9장](../09_time_series_models)에서도 사용할 것입니다.

### 코드 예: Wavelet을 사용하여 잡음이 있는 신호를 전처리하는 방법

[kalman_filter_and_wavelets](03_kalman_filter_and_wavelets.ipynb) 노트북은 [부록 - 알파 팩터 라이브러리](../24_alpha_factor_library) 패키지를 사용하여 웨이블릿으로 작업하는 방법도 보여줍니다.

### 자원

- [파마 프렌치](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) 데이터 라이브러리
- [멍청하다](https://numpy.org/) 웹사이트
    - __자리표시자_33__
- [팬더](https://pandas.pydata.org/) 웹사이트
    - __자리 표시자_35__
    - __자리표시자_36__
    - __자리표시자_37__
- [알파툴](https://github.com/marketneutral/alphatools) - Python의 정량적 금융 연구 도구
- [mlfinlab](https://github.com/hudson-and-thames/mlfinlab) - 금융 기계 학습의 발전에 관한 Marcos Lopez de Prado 박사의 연구 작업을 기반으로 한 패키지
- [피칼만](https://pykalman.github.io/) 문서
- __자리표시자_41__
- __자리표시자_42__
- __자리표시자_43__
- [PyWavelets](https://pywavelets.readthedocs.io/en/latest/) - Python의 웨이블릿 변환
- __자리표시자_45__ 
- __자리표시자_46__
- __자리표시자_47__
- __자리표시자_48__
- [적극적인 포트폴리오 관리: 우수한 수익 창출 및 위험 통제를 위한 정량적 접근 방식](https://www.amazon.com/Active-Portfolio-Management-Quantitative-Controlling/dp/0070248826) 작성자: Richard Grinold 및 Ronald Kahn, 1999
- [현대 투자 관리: 균형 접근 방식](https://www.amazon.com/Modern-Investment-Management-Equilibrium-Approach/dp/0471124109), Bob Litterman 작성, 2003
- [정량적 자산 포트폴리오 관리: 현대 기술 및 응용](https://www.crcpress.com/Quantitative-Equity-Portfolio-Management-Modern-Techniques-and-Applications/Qian-Hua-Sorensen/p/book/9781584885580) 작성자: Edward Qian, Ronald Hua, Eric Sorensen
- __자리표시자_52__

## 신호에서 거래까지: `Zipline`를 사용한 백테스팅

오픈 소스 [지퍼 라인](https://zipline.ml4trading.io/index.html) 라이브러리는 알고리즘 개발 및 실시간 거래를 촉진하기 위해 크라우드 소싱 정량 투자 펀드 [양자역학](https://www.quantopian.com/)에서 생산에 유지 관리하고 사용하는 이벤트 중심 백테스팅 시스템입니다. 이는 거래 이벤트에 대한 알고리즘의 반응을 자동화하고 예측 편향을 방지하는 현재 및 과거 시점 데이터를 제공합니다.

- [제8장](../08_ml4t_workflow)에는 Zipline에 대한 보다 포괄적인 소개가 포함되어 있습니다.
- **알려진 문제** 해결을 포함하여 `installation` 폴더의 [지침](../installation)을 따르세요.

### 코드 예: Zipline을 사용하여 단일 요소 전략을 백테스트하는 방법

노트북 [Single_factor_zipline](04_single_factor_zipline.ipynb)은 최근 성과가 과거 평균에서 얼마나 벗어났는지 측정하는 간단한 평균 회귀 요인을 개발하고 테스트합니다. 단기 반전은 주가 상승이 1분 미만에서 한 달까지 범위를 넘어 평균 복귀할 가능성이 있다는 약한 예측 패턴을 활용하는 일반적인 전략입니다.

### 코드 예: Quantopian 플랫폼에서 다양한 데이터 소스의 요소 결합

Quantopian 연구 환경은 예측 알파 요인의 신속한 테스트에 맞춰져 있습니다. 이 프로세스는 `zipline`를 기반으로 하기 때문에 매우 유사하지만 데이터 소스에 대한 훨씬 더 풍부한 액세스를 제공합니다.

The notebook [multiple_factors_Quantopian_research](05_multiple_factors_quantopian_research.ipynb) illustrates how to compute alpha factors not only from market data as previously but also from fundamental and alternative data.
    
### 코드 예: 신호와 잡음 분리 – 알파렌 사용 방법

노트북 [performance_eval_alphalens](06_performance_eval_alphalens.ipynb)에는 Quantopian이 오픈 소스로 제공하는 예측(알파) 요인의 성능 분석을 위한 [알파렌즈](http://quantopian.github.io/alphalens/) 라이브러리가 도입되었습니다. 이는 백테스팅 라이브러리 `zipline` 및 다음 장에서 살펴볼 포트폴리오 성능 및 위험 분석 라이브러리 `pyfolio`와 통합하는 방법을 보여줍니다.

`alphalens`은 다음에 관한 알파 요인의 예측력 분석을 용이하게 합니다.
- 후속 수익률과 신호의 상관관계
- 신호(의 하위 집합)를 기반으로 한 동일 또는 요인 가중 포트폴리오의 수익성
- 잠재적인 거래 비용을 나타내는 요소의 회전율
- 특정 이벤트 중 요인 성과
- 업종별 선행 분석

분석은 `tearsheets` 또는 개별 계산 및 플롯을 사용하여 수행할 수 있습니다. 공간을 절약하기 위해 테어시트가 온라인 저장소에 설명되어 있습니다.

- Quantopian의 자세한 `alphalens` 튜토리얼은 [여기](https://github.com/quantopian/alphalens/blob/master/alphalens/examples/alphalens_tutorial_on_quantopian.ipynb)을 참조하세요.

## 대체 알고리즘 거래 라이브러리 및 플랫폼

- __자리표시자_62__
- __자리표시자_63__
    - Alpha Trading Labs는 더 이상 활성화되지 않습니다.
- __자리표시자_64__
- Python 알고리즘 트레이딩 라이브러리 [PyAlgoTrade](http://gbeced.github.io/pyalgotrade/)
- __자리표시자_66__
- __자리표시자_67__
- __자리표시자_68__