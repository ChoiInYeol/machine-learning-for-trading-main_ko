# 합성 시계열 데이터를 위한 생성적 적대 신경망

이 장에서는 생성적 적대 신경망(GAN)을 소개합니다. GAN은 경쟁적인 환경에서 생성자와 판별자 네트워크를 훈련시켜 판별자가 주어진 훈련 데이터 클래스와 구별할 수 없는 샘플을 생성하는 방법을 생성자가 학습하도록 합니다. 목표는 이 클래스를 대표하는 합성 샘플을 생성할 수 있는 생성 모델을 생성하는 것입니다.
이미지 데이터에 가장 널리 사용되는 GAN은 의료 분야에서 합성 시계열 데이터를 생성하는 데에도 사용되었습니다. 재무 데이터를 사용한 후속 실험에서는 GAN이 ML 교육 또는 전략 백테스트에 유용한 대체 가격 궤적을 생성할 수 있는지 여부를 조사했습니다. 우리는 접근 방식을 설명하고 결과를 보여주기 위해 2019 NeurIPS Time-Series GAN 논문을 복제했습니다.

<p 정렬="중앙">
<img src="https://i.imgur.com/W1Rp89K.png" width="60%">
</p>

## 콘텐츠

1. __자리표시자_0__
    * __자리표시자_1__
    * __자리표시자_2__
2. __자리표시자_3__
3. __자리표시자_4__
    * __자리표시자_5__
    * __자리표시자_6__
    * __자리표시자_7__
    * __자리표시자_8__
    * __자리표시자_9__
4. __자리표시자_10__
    * __자리표시자_11__
    * __자리표시자_12__
    * __자리표시자_13__
    * __자리표시자_14__

## 합성 데이터를 위한 생성적 적대 신경망

이 책은 주로 입력 데이터를 받아 결과를 예측하는 지도 학습 알고리즘에 중점을 두고 있으며, 이를 실제와 비교하여 성능을 평가할 수 있습니다. 이러한 알고리즘은 서로 다른 출력 값을 구별하는 방법을 배우기 때문에 판별 모델이라고도 합니다.
생성적 적대 신경망(GAN)은 [마지막 장](../20_autoencoders_for_conditional_risk_factors)에서 접한 변형 오토인코더와 같은 생성 모델의 인스턴스입니다.

### 생성 모델과 차별 모델 비교

판별 모델은 입력 데이터 X가 주어졌을 때 결과 y를 구별하는 방법을 학습합니다. 즉, 데이터 p(y | X)가 주어졌을 때 결과의 확률을 학습합니다. 반면 생성 모델은 입력과 결과 p(y, X)의 결합 분포를 학습합니다.

생성 모델은 베이즈 규칙을 사용하여 어떤 클래스가 가장 가능성이 높은지 계산하는 판별 모델로 사용될 수 있지만([제10장](../10_bayesian_machine_learning) 참조), 보다 일반적인 생성 문제를 먼저 해결하는 것보다 예측 문제를 직접 해결하는 것이 더 나은 경우가 많습니다.

### 적대적 훈련: 속임수의 제로섬 게임

GAN의 주요 혁신은 데이터 생성 확률 분포를 학습하는 새로운 방법입니다. 알고리즘은 생성자와 판별자라고 불리는 두 개의 신경망 사이에서 경쟁적이거나 적대적인 게임을 설정합니다.

<p 정렬="중앙">
<img src="https://i.imgur.com/0vuUsY0.png" width="80%">
</p>

## 코드 예: TensorFlow 2를 사용하여 GAN을 구축하는 방법

Python을 사용하는 생성적 적대 신경망의 구현을 설명하기 위해 이 섹션 앞부분에서 설명한 DCGAN(심층 합성곱 GAN) 예제를 사용하여 13장에서 처음 접한 패션 MNIST 데이터 세트의 이미지를 합성합니다.

노트북 [deep_convolutional_generative_adversarial_network](01_deep_convolutional_generative_adversarial_network.ipynb)은 Python을 사용한 GAN 구현을 보여줍니다. DCGAN(Deep Convolutional GAN) 예제를 사용하여 패션 MNIST 데이터세트의 이미지를 합성합니다.

## 코드 예: TimeGAN: 합성 금융 데이터에 대한 적대적 훈련

합성 시계열 데이터를 생성하는 것은 이미지용 GAN을 설계할 때 직면하는 것 이상의 특정 과제를 제기합니다. 
시계열 데이터의 생성 모델은 픽셀 값이나 수많은 주식 가격과 같은 특정 지점의 변수에 대한 분포 외에도 하나의 관찰 시퀀스가 ​​다른 관찰 시퀀스를 따르는 방식을 형성하는 시간적 역학도 학습해야 합니다(토론 참조). 9장: [변동성 예측 및 통계 차익거래를 위한 시계열 모델](../09_time_series_models)).

2019년 12월 NeurIPS에서 발표된 윤(Yoon), Jarrett 및 van der Schaar의 최근 유망한 [연구](https://papers.nips.cc/paper/8789-time-series-generative-adversarial-networks.pdf)는 감독 및 비지도 훈련을 결합하여 시간 상관관계를 설명하는 것을 목표로 하는 새로운 [시계열 생성적 적대 신경망](https://papers.nips.cc/paper/8789-time-series-generative-adversarial-networks.pdf)(TimeGAN) 프레임워크를 소개합니다. 
모델은 훈련 중에 과거 데이터에서 샘플링하는 동안 관찰된 역학을 준수하도록 장려하는 지도 목표와 적대 목표를 모두 최적화하는 동시에 시계열 임베딩 공간을 학습합니다. 
저자는 과거 주가를 포함한 다양한 시계열에서 모델을 테스트한 결과 합성 데이터의 품질이 사용 가능한 대안의 품질보다 훨씬 우수하다는 사실을 발견했습니다.

### 기능과 시간에 따른 데이터 생성 과정 학습

시계열 데이터에 대한 성공적인 생성 모델은 각 시점의 특징의 단면적 분포와 시간 경과에 따른 이러한 특징 간의 종단적 관계를 모두 포착해야 합니다. 
방금 논의한 이미지 맥락에서 표현된 모델은 실제 이미지가 어떻게 보이는지뿐만 아니라 비디오에서와 같이 한 이미지가 다음 이미지에서 어떻게 발전하는지 학습해야 합니다.

### 시계열 임베딩을 통해 적대적 학습과 지도 학습 결합

순환(조건부) GAN과 같은 시계열 데이터를 생성하려는 이전 시도는 생성자와 판별자의 역할에서 순환 신경망(RNN, 19장 [다변량 시계열 및 감정 분석을 위한 RNN](../19_recurrent_neural_nets) 참조)에 의존했습니다.

TimeGAN은 DCGAN 예제에서 익숙한 실제 시퀀스와 합성 시퀀스 모두에 대한 감독되지 않은 적대적 손실과 원본 데이터에 대한 단계별 감독된 손실을 결합하여 시계열의 자동 회귀 특성을 명시적으로 통합합니다. 
목표는 과거 데이터의 한 시점에서 다음 현재 시점으로의 전환에 대한 분포를 학습하기 위한 모델에 보상을 제공하는 것입니다.

### TimeGAN 아키텍처의 네 가지 구성 요소

TimeGAN 아키텍처는 적대적 네트워크와 자동 인코더를 결합하므로 그림 21.4에 설명된 대로 네 가지 네트워크 구성 요소가 있습니다.
오토인코더: 임베딩 및 복구 네트워크
적대적 네트워크: 시퀀스 생성기 및 시퀀스 판별기 구성 요소
<p 정렬="중앙">
<img src="https://i.imgur.com/WqoXbr8.png" width="80%">
</p>

### TensorFlow 2를 사용하여 TimeGAN 구현

이 섹션에서는 방금 설명한 TimeGAN 아키텍처를 구현합니다. 저자는 TensorFlow 2로 포팅하는 TensorFlow 1을 사용하여 샘플 코드를 제공합니다. TimeGAN을 구축하고 훈련하려면 몇 가지 단계가 필요합니다.
1. 실제 및 무작위 시계열 입력 선택 및 준비
2. 주요 TimeGAN 모델 구성요소 생성
3. 세 가지 학습 단계에서 사용되는 다양한 손실 함수 및 학습 단계 정의
4. 훈련 루프 실행 및 결과 기록
5. 합성 시계열 생성 및 결과 평가

노트북 [시간GAN_TF2](02_TimeGAN_TF2.ipynb)에서는 이러한 단계를 구현하는 방법을 보여줍니다.

### 합성 시계열 데이터의 품질 평가

TimeGAN 작성자는 세 가지 실제 기준에 따라 생성된 데이터의 품질을 평가합니다.
1. **다양성**: 합성 샘플의 분포는 실제 데이터의 분포와 대략 일치해야 합니다.
2. **충실도**: 표본 계열은 실제 데이터와 구별할 수 없어야 합니다. 
3. **유용성**: 합성 데이터는 예측 작업을 해결하는 데 실제 데이터만큼 유용해야 합니다.

저자는 합성 데이터가 실제로 이러한 특성을 나타내는지 여부를 평가하기 위해 세 가지 방법을 적용합니다.
1. **시각화**: 다양성의 질적 다양성 평가를 위해 차원 축소(주성분 분석(PCA) 및 t-SNE, 13장 참조)를 사용하여 합성 샘플의 분포가 샘플의 분포와 얼마나 밀접하게 유사한지 시각적으로 검사합니다. 원본 데이터
2. **차별 점수**: 충실도의 정량적 평가를 위해 2-layer LSTM(18장 참조)과 같은 시계열 분류기의 테스트 오류를 ​​실제 시계열과 합성 시계열로 구별할 수 있는지 평가해 보겠습니다. 실제로는 구별이 불가능합니다.
3. **예측 점수**: 유용성을 정량적으로 측정하기 위해 실제 또는 합성 데이터로 훈련된 시퀀스 예측 모델의 테스트 오류를 ​​비교하여 실제 데이터의 다음 시간 단계를 예측할 수 있습니다.

노트북 [평가_합성_데이터](03_evaluating_synthetic_data.ipynb)에는 관련 코드 샘플이 포함되어 있습니다.

## 자원

### GAN의 작동 방식

- [NIPS 2016 튜토리얼: 생성적 적대 신경망](https://arxiv.org/pdf/1701.00160.pdf), 이안 굿펠로우, 2017
- [비지도 학습이 왜 중요한가요?](https://www.quora.com/Why-is-unsupervised-learning-important), 요슈아 벤지오(Quora), 2018
- [GAN Lab: 대화형 시각적 실험을 사용하여 복잡한 심층 생성 모델 이해](https://www.groundai.com/project/gan-lab-understanding-complex-deep-generative-models-using-interactive-visual-experimentation/), Minsuk Kahng, Nikhil Thorat, Duen Horng (Polo) Chau, Fernanda B. Viégas, Martin Wattenberg, 시각화 및 컴퓨터 그래픽에 관한 IEEE 트랜잭션, 25(1)(VAST 2018), 2019년 1월
    - __자리표시자_27__
- [생성적 적대 신경망](https://arxiv.org/abs/1406.2661), Ian Goodfellow 외, 2014
- [생성적 적대 신경망: 개요](https://arxiv.org/pdf/1710.07035.pdf), Antonia Creswell 외, 2017
- [생성 모델](https://blog.openai.com/generative-models/), OpenAI 블로그

### 구현

- __자리표시자_31__
- __자리표시자_32__
- [케라스-GAN](https://github.com/eriklindernoren/Keras-GAN), 다양한 Keras GAN 구현
- [PyTorch-GAN](https://github.com/eriklindernoren/PyTorch-GAN), 수많은 PyTorch GAN 구현

### GAN 아키텍처 동물원의 급속한 진화

- [DCGAN(Deep Convolutional Generative Adversarial Networks)을 사용한 비지도 표현 학습](https://arxiv.org/pdf/1511.06434.pdf), Luke Metz 외, 2016
- [조건부 생성적 적대망](https://arxiv.org/pdf/1411.1784.pdf), Medhi Mirza 및 Simon Osindero, 2014
- [Infogan: 생성적 적대 네트워크를 극대화하는 정보를 통한 해석 가능한 표현 학습](https://arxiv.org/pdf/1606.03657.pdf), Xi Chen 외, 2016
- [Stackgan: 누적 생성적 적대 신경망(Stacked Generative Adversarial Networks)을 사용한 텍스트를 사실적인 이미지 합성으로](https://arxiv.org/pdf/1612.03242.pdf), Shaoting Zhang 외, 2016
- [생성적 적대 신경망(Generative Adversarial Network)을 사용한 사실적인 단일 이미지 초해상도](https://arxiv.org/pdf/1609.04802.pdf), Alejando Acosta 외, 2016
- [주기 일치 적대 네트워크를 사용한 짝이 없는 이미지 간 변환](https://arxiv.org/pdf/1703.10593.pdf), Juan-Yan Zhu 외, 2018
- [무엇을, 어디서 그릴지 배우기](https://arxiv.org/abs/1610.02454), Scott Reed 외 2016
- __자리표시자_42__

### 응용

- [반복 조건부 GAN을 사용한 실제 값(의료) 시계열 생성](https://arxiv.org/abs/1706.02633), 크리스토발 에스테반, 스테파니 L. 하이랜드, 군나르 래치, 2016
    - __자리표시자_44__
- [MAD-GAN: 생성적 적대 신경망을 사용한 시계열 데이터에 대한 다변량 이상 탐지](https://arxiv.org/pdf/1901.04997.pdf), Dan Li, Dacheng Chen, Jonathan Goh, See-Kiong Ng, 2019
    - __자리표시자_46__
- [GAN — 몇 가지 멋진 애플리케이션](https://medium.com/@jonathan_hui/gan-some-cool-applications-of-gans-4c9ecca35900), 조나단 후이, 2018
- [Gans-Awesome-애플리케이션](https://github.com/nashory/gans-awesome-applications), 멋진 GAN 애플리케이션 선별 목록



