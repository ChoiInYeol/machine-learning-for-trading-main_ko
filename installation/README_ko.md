# 설치 지침

버전 충돌이 발생할 가능성이 높아지므로 모든 라이브러리를 한 번에 설치하려고 할 필요는 없습니다. 대신, 진행하면서 특정 장에 필요한 라이브러리를 설치하는 것이 좋습니다.

> 2022년 3월 업데이트: 이제 `zipline-reloaded`, `pyfolio-reloaded`, `alphalens-reloaded`, `empyrical-reloaded`을(를) `conda-forge` 채널에서 사용할 수 있습니다. `ml4t` 채널에는 오래된 버전만 포함되어 있으며 곧 삭제될 예정입니다.

> M1/실리콘 칩을 사용하는 MacOS에 대한 지원은 아직 불완전합니다. 새로운 아키텍처와 호환되는 일부 패키지는 `conda`/`mamba`을 통해서만 사용할 수 있고 다른 패키지는 `pip`을 통해서만 사용할 수 있습니다. 결과적으로 아직 단일 설치 스크립트가 없습니다. PyData 생태계 전반에 걸친 지원이 성숙해짐에 따라 이를 단순화할 수 있기를 바랍니다. 지금은 별도의 `conda`/`pip` 기반 환경을 만들어 필요에 따라 지원되는 패키지를 설치하세요.
 
> 2021년 9월 10일 업데이트: 최신 [지퍼 라인](https://github.com/stefan-jansen/zipline-reloaded), [알파렌즈](https://github.com/stefan-jansen/alphalens-reloaded) 및 [낭종](https://github.com/stefan-jansen/pyfolio-reloaded) 버전을 포함하는 `pip`(Linux, MacOS) 및 `conda`(Linux, MacOS, Windows) 설치용 새 OS 독립적 환경 파일 `ml4t-base.[txt, yml]`을 사용할 수 있습니다. 이러한 파일은 OS별 종속성이 아닌 기본 라이브러리만 포함하므로 OS에 구애받지 않으며, 최신 호환 버전과 OS별 종속성을 선택하는 패키지 관리자에게 맡깁니다.

> 2021년 4월 25일 업데이트: [새로운 집라인 버전](https://github.com/stefan-jansen/zipline-reloaded)을 사용하면 모든 운영 체제에서 Docker 없이 백테스트 노트북을 실행할 수 있습니다. 이제 설치 지침은 Windows/MacOS/Linux 환경 파일을 참조합니다.

> 2021년 3월 14일 업데이트: Python 3.7-3.9에서 실행되는 [새로운 집라인 버전](https://github.com/stefan-jansen/zipline-reloaded)을 방금 출시했습니다. [출시 정보](https://github.com/stefan-jansen/zipline-reloaded/releases/tag/2.0.0rc4) 및 [문서](https://zipline.ml4trading.io/)을 참조하세요. 결과적으로 앞으로는 Docker 솔루션이 더 이상 필요하지 않으며 4월 중에 새로운 환경 파일을 제공할 예정입니다.

> 2021년 2월 26일 업데이트: 릴리스 2.0은 환경 수를 2로 줄이고 기본 `ml4t`의 경우 Python 버전을 3.8로, `backtest` 환경의 경우 3.6으로 높입니다.
> 아래 지침에는 이러한 변경 사항이 반영되어 있습니다.
> 
> Docker 이미지를 최신 버전으로 업데이트하려면 다음을 실행하세요.
> __자리표시자_0__

이 책에서는 Python 3.8과 설치 가능한 다양한 ML 및 거래 관련 라이브러리를 사용합니다.

1. [미니콘다](https://docs.conda.io/en/latest/miniconda.html) 배포 및 제공된 `ml4t.yml` 환경 파일을 기반으로 [콘다 환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)에서 [맘바](https://github.com/mamba-org/mamba)을 사용하여,
   - OS 관련 파일에 문제가 발생하는 경우 대신 불가지론적인 `installation/ml4t-base.yml` 파일을 사용하세요.
   - 달리다:
   - __자리표시자_1__
2. macOS 및 Linux에만 해당: 제공된 `ml4t.txt` 요구 사항 파일을 사용하여 [피엔브](https://github.com/pyenv/pyenv) 또는 [벤브](https://docs.python.org/3/tutorial/venv.html)로 생성된 Python 가상 환경에서 [씨](https://pip.pypa.io/en/stable/)을 통해.
3. 더 이상 사용되지 않음: [도커](https://www.docker.com/) 데스크톱을 사용하여 [도커 허브](https://www.docker.com/products/docker-hub)에서 이미지를 가져오고 노트북을 실행하는 데 필요한 소프트웨어가 포함된 로컬 컨테이너를 만듭니다.

소스 코드를 얻는 방법을 설명하고 처음 두 가지 옵션을 차례로 배치합니다. 그런 다음 [주피터](https://jupyter.org/) 노트북을 사용하여 코드 예제를 보고 실행하는 방법을 설명합니다. 마지막으로 레거시 Docker 설치 지침을 나열합니다.

## 코드 샘플 소싱

[GitHub 저장소](https://github.com/stefan-jansen/machine-learning-for-trading)의 압축 버전을 다운로드하거나 해당 콘텐츠를 [복제](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/)하여 코드 샘플 작업을 할 수 있습니다. 후자는 커밋 기록을 포함하므로 다운로드 용량이 더 커집니다.

또는 저장소의 [포크](https://guides.github.com/activities/forking/)을 생성하고 해당 콘텐츠를 복제한 후 거기에서 계속 개발할 수 있습니다.

코드를 로컬에서 작업하려면 다음을 수행합니다.
1. 코드와 데이터를 저장하려는 파일 시스템 위치를 선택합니다.
2. `ssh` 또는 `https` 링크나 [GitHub 저장소](https://github.com/stefan-jansen/machine-learning-for-trading)의 녹색 `Code` 버튼이 제공하는 다운로드 옵션을 사용하여 대상 폴더에 코드를 복제하거나 압축을 풉니다.
    - 스타터 저장소를 복제하려면 `git clone https://github.com/stefan-jansen/machine-learning-for-trading.git`를 실행하고 새 디렉터리로 변경합니다.
    - 저장소를 복제하고 이름을 바꾸지 않은 경우 루트 디렉터리는 `machine-learning-for-trading`이 되고 ZIP 버전은 `machine-learning-for-trading-master`에 압축이 풀립니다.

## `conda` 환경을 사용하여 필수 라이브러리를 설치하는 방법

지침은 Anaconda의 [미니콘다](https://docs.conda.io/en/latest/miniconda.html) 배포판, 종속성 관리를 용이하게 하는 [맘바](https://github.com/mamba-org/mamba) 패키지 관리자, 고정된 라이브러리 버전이 있는 `installation/[windows|macos|linux]/ml4t.yml`의 OS별 환경 파일을 사용합니다.

또는 종속성 없이 필수 라이브러리 목록만 포함하는 환경 파일 `installation/ml4t-base.yml`도 있습니다. 대신 이 파일을 사용하면 최신 버전을 얻을 수 있습니다. 다만 어느 시점에서는 최신 소프트웨어가 예제와 호환되지 않을 수 있다는 점에 유의하세요.

관심 있는 노트북에 필요한 패키지를 설치할 수도 있습니다. 최신 버전(2021년 3월 현재)이 작동합니다.

### 미니콘다 설치

노트북은 먼저 설치해야 하는 [미니콘다3](https://docs.conda.io/en/latest/miniconda.html) 기반의 단일 가상 환경을 사용합니다.

다양한 운영 체제 [여기](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)에 대한 자세한 지침을 확인할 수 있습니다.

### 환경 파일에서 Conda 환경 만들기

[conda]는 [아나콘다](https://www.anaconda.com/) Python 배포판에서 제공하는 패키지 관리자입니다. 안타깝게도 현재는 [상태가 별로 좋지 않아](https://github.com/conda/conda/issues/9707)입니다. 대신, 더 빠르고 훨씬 빠른 [맘바](https://github.com/mamba-org/mamba) 패키지 관리자를 사용하여 패키지를 설치하겠습니다. 다음을 사용하여 설치할 수 있습니다.
__자리표시자_2__

노트북에 사용된 최신 버전의 라이브러리(2021년 4월 기준)로 [가상 환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)을 생성하려면 복제된 루트 디렉터리의 명령줄에서 다음 옵션 중 하나(운영 체제에 따라 다름)를 실행하면 됩니다. 저장소:

__자리표시자_3__

가상 환경에 대한 자세한 튜토리얼은 `ml4t`을 참조하세요.

이 글을 읽을 때마다 최신 라이브러리 버전으로 새 환경을 생성하려면 다음을 실행하세요.

__자리표시자_4__

### 콘다 환경 활성화

환경을 만든 후에는 해당 이름(이 경우 [여기](https://towardsdatascience.com/getting-started-with-python-environments-using-conda-32e9f2779307))을 사용하여 환경을 활성화할 수 있습니다.

__자리표시자_5__

비활성화하려면 간단히 다음을 사용하십시오.

__자리표시자_6__

## pip를 사용하여 라이브러리 설치

`apt`에 필수 라이브러리를 설치해야 합니다. 내장된 `export QUANDL_API_KEY=<your_key>` 옵션 또는 여러 Python 버전을 병렬로 실행할 수 있는 `.bash_profile` 대안에 대한 문서를 참조하세요.

일부 라이브러리에는 컴퓨터 상태에 따라 달라질 수 있는 OS별 소프트웨어의 이전 설치가 필요합니다. 아래에는 몇 가지 일반적인 사례가 나열되어 있습니다. 다른 문제가 발생하면 문제를 일으키는 라이브러리에 대한 설명서를 참조하세요. 그래도 문제가 해결되지 않는 경우 GitHub에서 문제를 제기해 주시면 여기에서 지침을 살펴보고 그에 따라 업데이트할 수 있습니다.

### 전제조건: MacOS

MacOS를 설치하려면 `ingest`를 통해 설치할 수 있는 다음 라이브러리가 필요합니다.
__자리표시자_7__

### 전제조건: 리눅스

Ubuntu에서는 [가상 환경](https://realpython.com/python-virtual-environments-a-primer/)를 통해 전제 조건을 충족할 수 있습니다. TA-Lib의 경우 `~/.zipline`은 다음과 같습니다.

__자리표시자_8__

### 요구 사항 설치

가상 환경을 생성하고 활성화했다고 가정하면 다음을 실행하기만 하면 됩니다(OS에 따라 다름).
__자리 표시자_9__

## 설치 후 지침

### QUANDL API 키 받기

다음 단계에서 책 전반에 걸쳐 여러 예시에 사용할 미국 주식 데이터를 다운로드하려면 개인 Quandl 계정에 대해 `ml4t`를 사용하여 API 키를 얻으세요. `python` 페이지에 표시됩니다.

Mac OSX와 같은 UNIX 기반 시스템을 사용하는 경우 QUANDL_API_KEY와 같은 환경 변수에 API 키를 저장할 수 있습니다. [피엔브](https://github.com/pyenv/pyenv)에 [벤브](https://docs.python.org/3/library/venv.html)을 추가하면 됩니다.

### 집라인 데이터 수집 중

Zipline 백테스트를 실행하려면 [집에서 만든 맥주](https://brew.sh/) 데이터가 필요합니다. 자세한 내용은 `ssh`을 참조하세요.

기본적으로 Zipline은 [필요한 단계](https://artiya4u.medium.com/installing-ta-lib-on-ubuntu-944d8ca24eae) 디렉터리 아래의 사용자 디렉터리에 데이터를 저장합니다.

명령 프롬프트에서 [등록하다](https://www.quandl.com/sign-up) 가상 환경을 활성화하고 다음을 실행합니다.
__자리표시자_10__

Zipline이 약 3,000개의 주가 시리즈를 처리하는 동안 수많은 메시지(무시할 수 있는 일부 경고 포함)가 표시됩니다.

### Jupyter 노트북 작업

이 섹션에서는 이 환경에서 작업을 용이하게 하는 노트북 확장을 설정하는 방법과 원하는 경우 노트북을 Python 스크립트로 변환하는 방법을 다룹니다.

#### jupyter 확장 설정

jupyter Notebook은 커뮤니티에서 제공하는 다양한 `https`을 사용할 수 있습니다. `Code`에 설명된 유용한 것들이 많이 있습니다.

이 저장소의 노트북은 `git clone https://github.com/stefan-jansen/machine-learning-for-trading.git` 확장자를 사용하도록 형식화되었습니다. 최상의 경험을 위해서는 jupyter 서버를 시작한 후 브라우저에서 사용할 수 있는 `machine-learning-for-trading` 탭의 구성기를 사용하여 활성화하세요. 기본적으로 설정되지 않은 경우 'ToC에서 h1 항목 제외' 옵션을 확인하도록 설정을 수정합니다.

#### jupyter 노트북을 Python 스크립트로 변환

이 책에서는 `machine-learning-for-trading-master` 노트북을 사용하여 광범위한 설명 및 컨텍스트 정보가 포함된 코드를 제시하고 결과를 한 곳에서 쉽게 시각화할 수 있습니다. 일부 코드 예제는 더 길며 [프로필](https://www.quandl.com/account/profile) 스크립트로 실행하는 것이 더 적합합니다. 명령줄에서 다음을 실행하여 노트북을 스크립트로 변환할 수 있습니다.

__자리표시자_11__

## 레거시 지침: Docker 컨테이너를 사용하여 노트북 실행

Docker Desktop은 다양한 OS에서 컨테이너화된 애플리케이션을 쉽게 공유할 수 있기 때문에 MacOS 및 Windows 시스템에서 매우 널리 사용되는 애플리케이션입니다. 이 책에는 호스트에 대한 종속성을 걱정하지 않고 Windows 10 또는 Mac OS X에 사전 설치된 `export QUANDL_API_KEY=<your_key>`을 사용하여 Ubuntu 20.04를 게스트 OS로 실행하기 위해 컨테이너를 인스턴스화할 수 있는 Docker 이미지가 있습니다.

### 도커 데스크탑 설치

평소와 같이 Mac OS X 및 Window 10의 경우 설치 방법이 다르며, Windows 10 Home의 경우 가상화를 활성화하려면 추가 단계가 필요합니다.

각 OS에 대한 설치를 별도로 다룬 다음 두 경우 모두 필요한 일부 설정 조정을 다룰 것입니다.

#### Mac OS X의 Docker 데스크탑

Mac OS X에 Docker Desktop을 설치하는 것은 매우 간단합니다.
1. Docker `.bash_profile`의 세부 가이드에 따라 `appliedai`에서 Docker Desktop을 다운로드하고 설치합니다. 또한 Docker Desktop 및 Docker Toolbox가 `packt` 방법을 다룹니다.
2. `ml4t` 튜토리얼에 따라 `latest`을 사용하세요.

터미널을 열고 다음 테스트를 실행하여 Docker가 작동하는지 확인하세요.
__자리표시자_12__

주요 설정 및 명령에 익숙해지려면 Mac OS용 `jupyter` 가이드를 검토하세요.

#### Windows의 Docker 데스크탑

Docker Desktop은 Windows 10 Home 및 Pro 버전 모두에서 작동합니다. Home 에디션에는 가상 머신 플랫폼을 활성화하는 추가 단계가 필요합니다.

##### Windows 10 Home: 가상 머신 플랫폼 활성화

이제 `/home/packt/ml4t`(WSL 2) 백엔드를 사용하여 Windows 홈 컴퓨터에 Docker Desktop을 설치할 수 있습니다. Windows Home의 Docker Desktop은 Linux 컨테이너 개발을 위한 Docker Desktop의 정식 버전입니다.

Windows 10 Home 컴퓨터는 특정 `QUANDL_API_KEY`을 충족해야 합니다. 여기에는 Windows 10 Home 버전 2004(2020년 5월 출시) 이상이 포함됩니다. Docker Desktop Edge 릴리스는 Windows 10 버전 1903 이상도 지원합니다.

`<your API key>`에 설명된 대로 다음 단계에 따라 WSL 2를 활성화합니다.

1. 선택적 Linux용 Windows 하위 시스템 기능을 활성화합니다. PowerShell을 관리자로 열고 다음을 실행합니다.
    __자리표시자_13__
2. 시스템이 `bash`에 설명된 요구 사항을 충족하는지 확인하고 필요한 경우 Windows 10 버전을 업데이트하세요.
3. 관리자 권한으로 PowerShell을 열고 다음을 실행하여 가상 머신 플랫폼 옵션 기능을 활성화합니다.
    __자리 표시자_14__
4. WSL 설치 및 WSL 2 업데이트를 완료하려면 컴퓨터를 다시 시작하세요.
5. Linux 커널 `packt`을 다운로드하고 실행합니다. 권한 상승을 요청하는 메시지가 표시되면 '예'를 선택하여 설치를 승인하세요.
6. 관리자 권한으로 PowerShell을 열어 새 Linux 배포판을 설치할 때 WSL 2를 기본 버전으로 설정하고 다음 명령을 실행합니다.
    __자리표시자_15__
  
##### Windows 10: Docker 데스크탑 설치

Windows Home용 WSL 2를 활성화한 후 Docker Desktop을 설치하는 나머지 단계는 Windows 10 `pwd` 및 `$QUANDL_API_KEY`에서 동일합니다. 시스템 요구 사항은 각 OS 버전에 대한 링크된 가이드를 참조하세요.

1. `C:/Users/stefan/Documents/machine-learning-for-trading`에서 설치 프로그램을 다운로드하고 실행(더블클릭)합니다.
2. 메시지가 표시되면 구성 페이지에서 Hyper-V Windows 기능 활성화 옵션이 선택되어 있는지 확인합니다.
3. 설치 마법사의 지침에 따라 설치 프로그램을 인증하고 설치를 진행합니다.
4. 설치가 성공적으로 완료되면 닫기를 클릭하여 설치 프로세스를 완료합니다.
5. 관리자 계정이 사용자 계정과 다른 경우 해당 사용자를 docker-users 그룹에 추가해야 합니다. 컴퓨터 관리를 관리자로 실행하고 로컬 사용자 및 그룹 > 그룹 > docker-users로 이동합니다. 그룹에 사용자를 추가하려면 마우스 오른쪽 버튼을 클릭하세요. 변경 사항을 적용하려면 로그아웃했다가 다시 로그인하세요.

Powershell을 열고 다음 테스트를 실행하여 Docker가 작동하는지 확인합니다.
__자리표시자_16__

주요 설정 및 명령에 익숙해지려면 Windows용 `C:\Users\stefan\Documents\machine-learning-for-trading` 가이드를 검토하세요.

### Docker 데스크탑 설정: 메모리 및 파일 공유

위에서 참조한 각 OS에 대한 시작 가이드에서는 Docker Desktop 설정을 설명합니다.

#### 메모리 늘리기

- 환경 설정에서 리소스를 찾아 컨테이너에 할당된 메모리를 늘릴 수 있는 방법을 알아보세요. 데이터 크기에 비해 기본 설정이 너무 낮습니다. 최소 4GB 이상, 8GB 이상으로 늘리세요.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
- 2장의 NASDAQ 틱 데이터 및 SEC 제출 예시와 같은 몇 가지 예시는 상당히 메모리 집약적이며 훨씬 더 높은 메모리 할당이 필요합니다.

#### 파일 공유 권한 문제 해결

코드 예제와 데이터를 호스트 OS의 로컬 드라이브에 다운로드하지만 로컬 드라이브를 볼륨으로 탑재하여 Docker 컨테이너에서 실행합니다. 현재 버전에서는 제대로 작동하지만 **권한 오류**가 발생하는 경우 Docker 사용자 가이드의 **파일 공유** 섹션을 참조하세요. Docker GUI를 사용하면 권한을 명시적으로 할당할 수 있습니다. (약간 오래된) 설명 `exit`도 참조하세요.
  
### 코드 샘플을 소싱하세요

`docker start -a -i ml4t`의 압축 버전을 다운로드하거나 해당 콘텐츠를 `conda env list`하여 코드 샘플을 사용할 수 있습니다. 후자는 커밋 기록을 포함하므로 다운로드 용량이 더 커집니다.

또는 저장소의 `base`을 생성하고 해당 콘텐츠를 복제한 후 거기에서 계속 개발할 수 있습니다.

코드를 로컬에서 작업하려면 다음을 수행합니다.
1. 코드와 데이터를 저장하려는 파일 시스템 위치를 선택합니다.
2. [초보자 튜토리얼](https://zipline.ml4trading.io/beginner-tutorial.html) 또는 [확대](https://github.com/ipython-contrib/jupyter_contrib_nbextensions) 링크나 `ml4t`의 녹색 [선적 서류 비치](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/) 버튼이 제공하는 다운로드 옵션을 사용하여 대상 폴더에 코드를 복제하거나 압축을 풉니다.
    - 스타터 저장소를 복제하려면 [목차(2)](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/toc2/README.html)을 실행하고 새 디렉터리로 변경합니다.
    - 저장소를 복제하고 이름을 바꾸지 않은 경우 루트 디렉터리는 [Nb 확장](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)이 되고 ZIP 버전은 [주피터](https://jupyter.org/)에 압축이 풀립니다.

### QUANDL API 키 받기

다음 단계에서 책 전반에 걸쳐 여러 예시에 사용할 미국 주식 데이터를 다운로드하려면 개인 Quandl 계정에 대해 `backtest`을 사용하여 API 키를 얻으세요. `backtest` 페이지에 표시됩니다.

Mac OSX와 같은 UNIX 기반 시스템을 사용하는 경우 QUANDL_API_KEY와 같은 환경 변수에 API 키를 저장할 수 있습니다. [문서](https://docs.docker.com/docker-for-mac/install/)에 [콘다 환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)을 추가하면 됩니다.

### Docker 이미지 다운로드 및 컨테이너 실행

우리는 `backtest`의 `conda install tensorflow-gpu` Python 배포판이 설치된 Ubuntu 20.04 OS 기반의 Docker `ml4t`를 사용할 것입니다. 아래에 설명된 두 가지 conda 환경이 함께 제공됩니다.

단일 Docker 명령을 사용하면 여러 가지 작업을 동시에 수행할 수 있습니다(자세한 내용은 위에 링크된 시작하기 가이드 참조).
- 첫 번째 실행 시에만: Docker Hub 계정 [도커 허브](https://hub.docker.com/editions/community/docker-ce-desktop-mac/) 및 저장소 [공존할 수 있다](https://docs.docker.com/docker-for-mac/docker-toolbox/)에서 태그 [집에서 만든 맥주](https://brew.sh/)을 사용하여 Docker 이미지를 가져옵니다. 
- [여기](https://aspetraining.com/resources/blog/docker-on-mac-homebrew-a-step-by-step-tutorial) 이름으로 로컬 컨테이너를 생성하고 대화형 모드에서 실행하여 [시작하기](https://docs.docker.com/docker-for-mac/) 서버에서 사용하는 포트 8888을 전달합니다.
- 시작 프로젝트 파일이 포함된 현재 디렉터리를 컨테이너 내부의 [Linux용 Windows 하위 시스템](https://fossbytes.com/what-is-windows-subsystem-for-linux-wsl/) 디렉터리에 볼륨으로 마운트합니다.
- 환경 변수 [요구 사항](https://docs.docker.com/docker-for-windows/install-windows-home/#system-requirements)를 키 값([여기](https://docs.microsoft.com/en-us/windows/wsl/install-win10)에 입력해야 하는 값)으로 설정하고
- 컨테이너 내부에서 [여기](https://docs.microsoft.com/en-us/windows/wsl/install-win10#requirements) 터미널을 시작하면 [업데이트 패키지](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) 사용자에 대한 새 명령 프롬프트가 표시됩니다.

1. 터미널 또는 Powershell 창을 엽니다.
2. 위에서 제공한 `conda activate <env_name>` 코드 샘플이 포함된 디렉터리로 이동합니다.
3. 로컬 버전 리포지토리의 루트 디렉터리에서 Mac 및 Windows에 필요한 다양한 경로 형식을 고려하여 다음 명령을 실행합니다.
    - **Mac OS**: [집](https://docs.docker.com/docker-for-windows/install-windows-home/) 명령을 현재 작업 디렉터리에 대한 절대 경로가 포함된 셸 변수로 사용할 수 있습니다(이전 단계에서 이러한 환경 변수를 만든 경우 [전문가, 기업 또는 교육](https://docs.docker.com/docker-for-windows/install-windows-home/)를 사용할 수 있습니다).  
        __자리표시자_17__
   - **Windows**: 현재 디렉터리의 절대 경로를 **슬래시**와 함께 입력하세요. [시작하기](https://docs.docker.com/docker-for-windows/) 대신 [도커 허브](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)을 사용하면 명령이 다음과 같이 됩니다(이 예의 경우).                                                                                                                                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                                                                                                                                  
     __자리표시자_18__              
4. 컨테이너 셸에서 [여기](https://rominirani.com/docker-on-windows-mounting-host-directories-d96f3f056a2c)을 실행하여 컨테이너를 종료하고 중지합니다. 
5. 작업을 재개하려면 루트 디렉터리의 Mac OS 터미널 또는 Windows Powershell에서 [GitHub 저장소](https://github.com/stefan-jansen/machine-learning-for-trading)를 실행하여 컨테이너를 다시 시작하고 대화형 모드에서 호스트 셸에 연결할 수 있습니다(자세한 내용은 Docker 문서 참조).

> Docker 이미지를 최신 버전으로 업데이트하려면 다음을 실행하세요.
> __자리표시자_19__

### 컨테이너에서 노트북 실행

이제 컨테이너 내부에서 셸을 실행 중이며 `conda init bash`에 모두 액세스할 수 있습니다. [복제](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/)을 실행하여 [포크](https://guides.github.com/activities/forking/), [GitHub 저장소](https://github.com/stefan-jansen/machine-learning-for-trading)(기본값) 및 [등록하다](https://www.quandl.com/sign-up) 환경이 있는지 확인하세요.

최신 버전의 Zipline 1.4.1은 부분적으로 컴파일이 필요한 다양한 기타 종속성의 Python 3.6 및 이전 버전만 지원하므로 [프로필](https://www.quandl.com/account/profile) 환경이 필요합니다. 앞으로 Python 3.8에서도 실행되도록 Zipline을 업데이트하고 싶습니다.

Zipline에서 생성된 Zipline 직접 입력을 사용하는 백테스팅 관련 노트북 12개를 제외하고는 [영상](https://hub.docker.com/repository/docker/appliedai/packt) 환경을 사용합니다. [아나콘다](https://www.anaconda.com/) 환경이 필요한 노트북에는 알림이 포함되어 있습니다.

> 딥 러닝 예제에 GPU를 사용하려는 경우 적절한 `source .bashrc`이 설치되어 있으면 [미니콘다](https://docs.conda.io/en/latest/miniconda.html)을 실행할 수 있습니다. 
> **또는** `ingest` 이미지를 활용하고 여기에 추가 라이브러리를 설치할 수 있습니다. DL 예제에는 설치가 지나치게 복잡한 것이 필요하지 않습니다.

- [ML4T](https://github.com/stefan-jansen/machine-learning-for-trading)을 사용하거나 `.zipline` 확장 덕분에 Jupyter Notebook 또는 Jupyter Lab 커널 메뉴를 사용하여 다른 환경으로 전환할 수 있습니다(아래 참조).
- [콘다 환경](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)을(를) 실행하라는 오류 메시지가 나타날 수 있습니다. 그런 다음 [CUDA 버전](https://www.tensorflow.org/install/source#gpu) 명령을 사용하여 셸을 다시 로드합니다.

### 집라인 데이터 수집 중

Zipline 백테스트를 실행하려면 [TensorFlow의 도커](https://www.tensorflow.org/install/docker) 데이터가 필요합니다. 자세한 내용은 `assets-7.sqlite`을 참조하세요.

이미지는 컨테이너를 시작한 디렉터리(위에서 다운로드한 시작 코드의 루트 폴더여야 함)의 [nb_conda_kernels](https://github.com/Anaconda-Platform/nb_conda_kernels) 디렉터리에 데이터를 저장하도록 구성되었습니다.

컨테이너 셸의 명령 프롬프트에서 다음을 실행합니다.
__자리표시자_20__ 
Zipline이 약 3,000개의 주가 시리즈를 처리하는 동안 수많은 메시지가 표시됩니다.

#### 알려진 집라인 문제

> `US`에서 다음 국가 코드 문제를 패치했으므로 더 이상 자산 데이터베이스를 수동으로 조작할 필요가 없습니다.

백테스트를 실행할 때 현재 Zipline 버전에서는 자산 메타데이터를 저장하는 [초보자 튜토리얼](https://zipline.ml4trading.io/beginner-tutorial.html) 데이터베이스의 교환 테이블에 국가 코드 항목이 필요하기 때문에 `country_code`이 발생할 가능성이 높습니다.

연결된 `assets-7.sqlite`에서는 `~/machine-learning-for-trading/data/.zipline/data/quandl/2020-12-29T02;06;08.894865/`을 열고 교환 테이블의 [오류](https://github.com/quantopian/zipline/issues/2517) 필드에 [최신 집라인 버전](https://github.com/stefan-jansen/zipline/commit/b33e5c955a58d888f55101874f45cd141c61d3e1)을 입력하여 이 문제를 해결하는 방법을 설명합니다.

실제로 이는 다음과 같습니다.

1. `exchanges`을 사용하여 최신 번들 다운로드가 포함된 디렉터리에서 [GitHub 문제](https://github.com/quantopian/zipline/issues/2517) 파일을 엽니다. 방금 설명한 대로 명령을 실행하면 경로는 다음과 같습니다(Linux/Max OSX에서): [SQLite 데이터베이스](https://sqlitebrowser.org/dl/)
2. 다음 스크린샷에 설명된 대로 [SQLite 브라우저](https://sqlitebrowser.org/dl/) 테이블을 선택합니다.
<p 정렬="중앙">
<img src="https://i.imgur.com/khq6gtX.png" title="QUANDL SQLite 수정 - 1단계" width="50%"/>
</p>
3. 국가 코드를 입력하고 결과를 저장합니다(프로그램을 닫을 때 메시지가 표시됩니다).
<p 정렬="중앙">
<img src="https://i.imgur.com/mtdiylk.png" title="QUANDL SQLite 수정 - 1단계" width="50%"/>
</p>

그게 다야. 안타깝게도 `zipline ingest -b quandl`을 실행할 때마다 이 작업을 반복해야 합니다. 이 오류는 기본 `quantopian-quandl` 번들에 대해 `zipline ingest`을 실행할 때 계속 발생합니다. 이 명령은 `ingest` 프로세스를 우회하고 이전 버전의 Zipline에서 생성된 결과의 압축된 버전을 대신 다운로드하기 때문입니다.

### Docker 컨테이너에서 노트북 작업

기존 [공책](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) 또는 최신 [주피터 연구소](https://jupyterlab.readthedocs.io/en/stable/) 인터페이스를 사용하여 [주피터](https://jupyter.org/) 노트북을 실행할 수 있습니다. 둘 다 모든 `conda` 환경에서 사용할 수 있습니다. 또한 `base` 환경에서 jupyter를 시작하고 `nb_conda_kernels` 패키지로 인해 노트북에서 환경을 전환합니다([문서](https://github.com/Anaconda-Platform/nb_conda_kernels) 참조).

시작하려면 다음 두 명령 중 하나를 실행하세요.
__자리표시자_21__
각각에 대한 `alias` 단축키도 있으므로 입력할 필요가 없습니다. 
- `jupyter notebook` 버전의 경우 `nb` 
- `jupyter lab` 버전의 경우 `lab`입니다.

jupyter 서버를 가동하는 동안 컨테이너 터미널에 몇 가지 메시지가 표시됩니다. 완료되면 현재 작업 디렉터리에서 jupyter 서버에 액세스하기 위해 브라우저에 붙여넣어야 하는 URL이 표시됩니다.

아래에 설명된 표준 conda 작업 흐름을 사용하여 모든 환경을 수정할 수 있습니다. 변경 후 컨테이너를 유지하는 방법은 Docker [문서](https://docs.docker.com/storage/)을 참조하세요.