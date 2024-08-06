# 거래를 위한 딥러닝

이 장에서는 몇 가지 딥 러닝(DL) 모델링 기술이 투자 및 거래에 어떻게 유용할 수 있는지 다루는 4부를 시작합니다. DL은 이미지 및 음성 인식부터 광범위한 관심을 끌고 인공 지능(AI)에 대한 대규모 연구를 부활시킨 로봇 공학 및 지능형 에이전트에 이르기까지 다양한 영역에서 수많은 혁신을 달성했습니다. 급속한 발전이 계속되고 어려운 현실적 문제에 대한 더 많은 해결책이 등장할 것이라는 기대가 높습니다.

이 장에서는 다음 장에서 다루는 다양한 DL 아키텍처와 관련된 신경망 작업의 핵심 요소를 소개하기 위해 피드포워드 신경망을 소개합니다. 보다 구체적으로 역전파 알고리즘을 사용하여 대규모 모델을 효율적으로 훈련하고 과적합 위험을 관리하는 방법을 보여줍니다. 또한 4부 전체에서 활용할 인기 있는 Keras, TensorFlow 2.0 및 PyTorch 프레임워크를 사용하는 방법을 보여줄 것입니다.

다음 장에서는 대체 텍스트 및 이미지 데이터에 특히 중점을 두고 다양한 투자 애플리케이션에 적합한 다양한 아키텍처를 설계하기 위해 이 기반을 구축할 것입니다. 여기에는 시계열이나 자연어와 같은 순차 데이터에 맞춰진 순환 신경망(RNN)과 이미지 데이터에 특히 적합하지만 시계열 데이터에도 사용할 수 있는 CNN(Convolutional Neural Network)이 포함됩니다. 또한 자동 인코더 및 GAN(Generative Adversarial Networks)을 포함한 심층 비지도 학습과 환경에서 대화형으로 학습하는 에이전트를 훈련시키는 강화 학습도 다룹니다.

## 콘텐츠

1. __자리표시자_0__
    * __자리표시자_1__
    * __자리표시자_2__
    * __자리표시자_3__
2. __자리표시자_4__
    * __자리표시자_5__
    * __자리표시자_6__
    * __자리표시자_7__
3. __자리표시자_8__
    * __자리표시자_9__
    * __자리표시자_10__
    * __자리표시자_11__
    * __자리표시자_12__
4. __자리표시자_13__
    * __자리표시자_14__
    * __자리표시자_15__

## 딥러닝의: 차이점과 중요한 이유

2부에서 다루는 기계 학습(ML) 알고리즘은 3부에서 설명한 텍스트 데이터를 포함하여 다양한 중요한 문제에서 잘 작동합니다. 그러나 음성 인식이나 분류와 같은 핵심 AI 문제를 해결하는 데는 덜 성공적이었습니다. 이미지 속 개체. 이러한 한계는 딥러닝 개발의 동기가 되었으며, 최근 딥러닝의 획기적인 발전은 AI에 대한 관심이 다시 높아지는 데 크게 기여했습니다. 에프

또는 이 섹션의 많은 요점을 포함하고 확장하는 포괄적인 소개는 Goodfellow, Bengio 및 Courville(2016)을 참조하거나 훨씬 짧은 버전은 LeCun, Bengio 및 Hinton(2015)을 참조하십시오.

- [딥러닝](https://www.deeplearningbook.org/), Ian Goodfellow, Yoshua Bengio 및 Aaron Courville, MIT Press, 2016
- [딥러닝](https://www.nature.com/articles/nature14539), Yann LeCun, Yoshua Bengio, Geoffrey Hinton, Nature 2015
- [신경망과 딥러닝](http://neuralnetworksanddeeplearning.com/), 마이클 A. 닐슨, Determination Press, 2015
- [인공지능 탐구 - 아이디어와 성과의 역사](https://ai.stanford.edu/~nilsson/QAI/qai.pdf), Nils J. Nilsson, Cambridge University Press, 2010
- __자리표시자_20__
- [TensorFlow 플레이그라운드](http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.71056&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false), 대화형 브라우저 기반 딥 러닝 플랫폼

### 계층적 기능이 고차원 데이터를 길들이는 데 어떻게 도움이 되는지

2부에서 논의한 것처럼 지도 학습의 주요 과제는 훈련 데이터를 새로운 샘플로 일반화하는 것입니다. 데이터의 차원이 증가할수록 일반화는 기하급수적으로 더 어려워집니다. 우리는 13장 [비지도 학습: 데이터 기반 위험 요소에서 계층적 위험 동등성까지](../13_unsupervised_learning)에서 차원의 저주로서 이러한 어려움의 근본 원인을 만났습니다.

### 특징 추출 자동화: 표현 학습으로서의 DL

이미지나 음성 인식과 같은 많은 AI 작업에는 세상에 대한 지식이 필요합니다. 주요 과제 중 하나는 이러한 지식을 컴퓨터가 활용할 수 있도록 인코딩하는 것입니다. 수십 년 동안 ML 시스템을 개발하려면 원시 데이터(예: 이미지 픽셀)를 학습 알고리즘이 패턴을 감지하거나 분류하는 데 사용할 수 있는 내부 표현으로 변환하기 위해 상당한 도메인 전문 지식이 필요했습니다.

### DL이 기계 학습 및 인공 지능과 어떻게 관련되는지

AI는 학술 분야로서 적어도 1950년대까지 거슬러 올라가고 인간 탐구의 주제로서 훨씬 더 오랫동안 거슬러 올라가는 오랜 역사를 가지고 있지만 그 이후로 여러 번의 쇠퇴와 흐름의 열풍을 경험해 왔습니다(자세한 내용은 [인공 지능에 대한 탐구](https://ai.stanford.edu/~nilsson/QAI/qai.pdf), Nilsson, 2009 참조). 조사). 
- ML은 통계 등 관련 학문에서 오랜 역사를 지닌 중요한 하위분야로 1980년대에 부각됐다. 
- DL은 표현 학습의 한 형태이며 그 자체가 ML의 하위 분야입니다.

## 코드 예: 신경망 설계

NN의 작동 방식을 더 잘 이해하기 위해 노트북 [01_build_and_train_feedforward_nn](build_and_train_feedforward_nn.ipynb)는 행렬 대수를 사용하여 간단한 피드포워드 아키텍처 및 순방향 전파 계산을 공식화하고 선형 대수의 Python 대응인 Numpy를 사용하여 이를 구현합니다.

<p 정렬="중앙">
<img src="https://i.imgur.com/UKCr9zi.png" width="85%">
</p>

### 주요 디자인 선택

일부 NN 설계 선택은 다른 지도 학습 모델의 선택과 유사합니다. 예를 들어 회귀, 분류, 순위 등 ML 문제 유형에 따라 출력이 결정됩니다. 출력이 주어지면 예측 성공 및 실패를 측정하기 위한 비용 함수와 비용을 최소화하기 위해 네트워크 매개변수를 최적화하는 알고리즘을 선택해야 합니다.

NN별 선택에는 레이어 수와 레이어당 노드 수, 서로 다른 레이어의 노드 간 연결, 활성화 함수 유형이 포함됩니다.

### 심층 신경망을 정규화하는 방법

임의 함수에 근접하는 NN 용량의 단점은 과적합 위험이 크게 증가한다는 것입니다. 과적합을 방지하는 가장 좋은 방법은 더 큰 데이터 세트에서 모델을 교육하는 것입니다. 데이터 증대(예: 약간 수정된 버전의 이미지를 생성하는 것은 강력한 대안 접근 방식입니다. 이러한 목적을 위한 합성 금융 교육 데이터 생성은 우리가 [21장](../21_gans_for_synthetic_time_series)에서 다룰 활발한 연구 분야입니다.

### 더 빠른 훈련: 딥 러닝을 위한 최적화

역전파는 업데이트하려는 내부 매개변수에 대한 비용 함수의 기울기 계산과 이 정보를 사용하여 매개변수 값을 업데이트하는 것을 의미합니다. 기울기는 비용 함수의 최대 증가를 유발하는 매개변수 변경 방향을 나타내기 때문에 유용합니다. 따라서 음의 기울기에 따라 매개변수를 조정하면 적어도 관찰된 샘플에 매우 가까운 영역에 대해 최적의 비용 절감이 가능합니다. 주요 경사하강법 최적화 알고리즘에 대한 훌륭한 개요는 Ruder(2016)를 참조하세요.

- [그라데이션 검사 및 고급 최적화](http://ufldl.stanford.edu/wiki/index.php/Gradient_checking_and_advanced_optimization), 비지도 기능 학습 및 딥 러닝, 스탠포드 대학교
- [경사하강법 최적화 알고리즘 개요](http://ruder.io/optimizing-gradient-descent/index.html#momentum), 세바스찬 루더, 2016

## 인기 있는 딥 러닝 라이브러리

현재 가장 널리 사용되는 DL 라이브러리는 [텐서플로우](https://www.tensorflow.org/)(Google에서 지원) 및 [파이토치](https://pytorch.org/)(Facebook에서 지원)입니다.

2020년 3월 현재 PyTorch 버전 1.4와 TensorFlow 2.2의 개발이 매우 활발합니다. TensorFlow 2.0은 [딱딱한](https://keras.io/)을 기본 인터페이스로 채택하여 두 라이브러리를 하나로 효과적으로 결합했습니다.
추가 옵션은 다음과 같습니다.

- __자리표시자_31__
- __자리표시자_32__
- [테나오](http://www.deeplearning.net/software/theano/), 2007년부터 몬트리올 대학교에서 개발
- [아파치 MXNet](https://mxnet.apache.org/), Amazon에서 사용
- [체이너](https://chainer.org/), 일본 회사 Preferred Networks에서 개발
- [토치](http://torch.ch/), PyTorch의 기반인 Lua를 사용합니다.
- [딥러닝4J](https://deeplearning4j.org/), Java 사용

### GPU 최적화를 활용하는 방법

널리 사용되는 모든 딥 러닝 라이브러리는 GPU 사용을 지원하며 일부는 여러 GPU에서 병렬 교육도 허용합니다. 가장 일반적인 유형의 GPU는 NVIDIA에서 생산되며 구성에는 CUDA 환경의 설치 및 설정이 필요합니다. 프로세스는 계속 발전하고 있으며 컴퓨팅 환경에 따라 다소 어려울 수 있습니다.

GPU를 활용하는 보다 간단한 방법은 Docker 가상화 플랫폼을 이용하는 것입니다. Docker가 관리하는 로컬 컨테이너에서 실행할 수 있는 수많은 이미지가 있어 발생할 수 있는 많은 드라이버 및 버전 충돌을 피할 수 있습니다. Tensorflow는 웹사이트에서 Keras와 함께 사용할 수 있는 도커 이미지를 제공합니다.

- [딥 러닝을 위해 어떤 GPU를 구입해야 할까요: 딥 러닝에서 GPU 사용에 대한 나의 경험과 조언](http://timdettmers.com/2018/11/05/which-gpu-for-deep-learning/), 팀 데트머스
- [딥 러닝에 대한 전체 하드웨어 가이드](http://timdettmers.com/2018/12/16/deep-learning-hardware-guide/), 팀 데트머스

### 텐서보드 사용 방법

Tensorboard는 TensorFlow와 함께 제공되는 훌륭한 시각화 도구입니다. 여기에는 신경망의 이해, 디버깅 및 최적화를 단순화하는 시각화 도구 모음이 포함되어 있습니다.

이를 사용하여 계산 그래프를 시각화하고, 다양한 실행 및 성능 지표를 플롯하고, 네트워크에서 처리된 이미지 데이터를 시각화할 수도 있습니다. 또한 다양한 훈련 실행을 비교할 수도 있습니다.
How_to_use_keras 노트북을 실행하고 TensorFlow가 설치된 경우 명령줄에서 Tensorboard를 시작할 수 있습니다.

__자리표시자_0__
- __자리표시자_40__

### 코드 예: PyTorch 사용 방법

Pytorch는 Yann LeCunn이 이끄는 Facebook AI Research 그룹에서 개발되었으며 2016년 9월에 출시된 첫 번째 알파 버전입니다. Pytorch는 기능 확장, 강력한 GPU 가속 및 자동 차별화에 사용할 수 있는 Numpy와 같은 Python 라이브러리와의 긴밀한 통합을 제공합니다. 오토그라드 시스템. 낮은 수준의 API를 통해 Keras보다 더 세부적인 제어를 제공하며 주로 딥러닝 연구 플랫폼으로 사용되지만 GPU 계산을 활성화하면서 NumPy를 대체할 수도 있습니다.

예를 들어 Theano 또는 TensorFlow에서 사용되는 정적 계산 그래프와 달리 즉시 실행을 사용합니다. 빠르지만 정적인 실행을 위해 처음에 네트워크를 정의하고 컴파일하는 대신, Tensor 작업의 자동 차별화를 위해 autograd 패키지를 사용합니다. 즉, 네트워크 구조를 더 쉽게 부분적으로 수정할 수 있도록 '즉시' 기울기를 계산합니다. 이를 실행별 정의라고 합니다. 즉, 역전파는 코드 실행 방식에 따라 정의되며, 이는 모든 단일 반복이 다를 수 있음을 의미합니다. PyTorch 문서는 이에 대한 자세한 튜토리얼을 제공합니다.

[How_to_use_pytorch](03_how_to_use_pytorch.ipynb) 노트북은 1.4 릴리스를 사용하는 방법을 보여줍니다.

- __자리표시자_42__
- __자리표시자_43__
- __자리표시자_44__
    - [AllenNLP](https://allennlp.org/), Allen Institute for Artificial Intelligence에서 개발한 최첨단 NLP 플랫폼
    - [예민한 후각](https://github.com/zalandoresearch/flair), Zalando에서 개발된 최첨단 NLP를 위한 간단한 프레임워크
    - [fst.ai](http://www.fast.ai/), 최신 모범 사례를 사용하여 NN 교육을 단순화합니다. 온라인 교육을 제공합니다

### 코드 예: TensorFlow 사용 방법

TensorFlow는 PyTorch보다 1년 전인 2015년 9월 출시된 직후 최고의 딥 러닝 라이브러리가 되었습니다. TensorFlow 2.0은 2017년부터 contrib 패키지의 일부로 TensorFlow에 통합된 Keras API를 주요 인터페이스로 만들고 즉시 실행을 채택함으로써 시간이 지남에 따라 점점 더 복잡해지는 API를 단순화하는 것을 목표로 합니다. 다양한 플랫폼에 걸친 강력한 구현에 계속 초점을 맞추겠지만 실험과 연구 수행이 더 쉬워질 것입니다.

[How_to_use_tensorflow](04_how_to_use_tensorflow.ipynb) 노트북은 2.0 릴리스를 사용하는 방법을 보여줍니다.

- __자리표시자_49__
- __자리표시자_50__
- [TensorFlow.js](https://js.tensorflow.org/), 브라우저와 Node.js에서 ML 모델을 훈련하고 배포하기 위한 JavaScript 라이브러리

## 코드 예: 장단기 거래 전략을 위한 신경망 최적화

실제로 어떤 구성이 데이터에 가장 적합한지 처음부터 확신할 수 없기 때문에 NN 아키텍처에 대한 설계 옵션의 변형과 이전에 설명한 것에서 이를 훈련하는 방법을 탐색해야 합니다.

이 코드 예제에서는 [제12장](../12_gradient_boosting_machines)에서 개발된 데이터 세트를 사용하여 일일 주식 수익률을 예측하기 위한 간단한 피드포워드 신경망의 다양한 아키텍처를 탐색합니다(노트북 [준비_the_model_data](../12_gradient_boosting_machines/04_preparing_the_model_data.ipynb) 참조).

이를 위해 여러 아키텍처 입력 매개변수를 기반으로 TensorFlow 모델을 반환하는 함수를 정의하고 7장에서 소개한 MultipleTimeSeriesCV를 사용하여 대체 설계를 교차 검증합니다. 모델 예측의 신호 품질을 평가하기 위해 간단한 순위를 작성합니다. - 샘플 내 교차 검증 기간 동안 가장 좋은 성능을 발휘하는 모델의 앙상블을 기반으로 하는 롱-숏 전략입니다. 잘못된 발견의 위험을 제한하기 위해 샘플 외 테스트 기간 동안 이 전략의 성능을 평가합니다.

### NN 아키텍처 최적화

[How_to_optimize_a_NN_architecure](04_how_to_use_tensorflow.ipynb) 노트북은 자산 수익률을 예측하기 위한 간단한 피드포워드 신경망을 구축하는 다양한 옵션을 탐색합니다. 거래 전략을 개발하기 위해 우리는 2010년부터 2017년까지 8년 동안 995개 미국 주식의 일일 주식 수익률을 사용합니다.

### 앙상블 신호를 기반으로 한 롱-숏 전략 백테스팅

NN 모델을 거래 전략으로 변환하기 위해 예측을 생성하고, 신호 품질을 평가하고, 이러한 예측에 따라 거래하는 방법을 정의하는 규칙을 만들고, 이러한 규칙을 구현하는 전략의 성과를 백테스트합니다.

노트북 [백테스팅_with_zipline](05_backtesting_with_zipline.ipynb)에는 이 섹션에 대한 코드 예제가 포함되어 있습니다.