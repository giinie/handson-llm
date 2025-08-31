# 용어사전 (Glossary)

핸즈온 LLM 프로젝트에서 사용되는 주요 용어들의 한국어/영어 대역 및 설명

## A-E

### AI/ML 기본 용어
- **인공지능** (Artificial Intelligence, AI) - 인간의 지능을 모방하는 컴퓨터 시스템
- **머신러닝** (Machine Learning, ML) - 데이터로부터 자동으로 학습하는 알고리즘
- **딥러닝** (Deep Learning, DL) - 신경망을 기반으로 한 머신러닝 방법론
- **어텐션** (Attention) - 입력의 중요한 부분에 집중하는 메커니즘
- **임베딩** (Embedding) - 텍스트나 단어를 벡터로 변환하는 기법

## F-L

### 모델 및 아키텍처
- **파인튜닝** (Fine-tuning) - 사전 훈련된 모델을 특정 작업에 맞게 추가 훈련
- **대규모 언어 모델** (Large Language Model, LLM) - 대량의 텍스트로 훈련된 거대한 신경망 모델
- **생성형 AI** (Generative AI) - 새로운 콘텐츠를 생성하는 인공지능
- **언어 모델** (Language Model, LM) - 언어의 확률 분포를 학습하는 모델

## M-R

### 훈련 및 최적화
- **사전 훈련** (Pre-training) - 대량의 데이터로 모델을 기본적으로 훈련하는 과정
- **프롬프트 엔지니어링** (Prompt Engineering) - 모델에게 효과적인 지시를 주는 기법
- **퓨샷 학습** (Few-shot Learning) - 적은 예시로 새로운 작업을 학습하는 방법
- **제로샷 학습** (Zero-shot Learning) - 예시 없이 새로운 작업을 수행하는 능력
- **강화학습** (Reinforcement Learning, RL) - 보상을 통해 학습하는 방법론
- **인간 피드백 강화학습** (Reinforcement Learning from Human Feedback, RLHF) - 인간의 평가를 기반으로 한 강화학습

## S-Z

### 기술적 구현
- **트랜스포머** (Transformer) - 어텐션 메커니즘 기반의 신경망 아키텍처
- **토크나이저** (Tokenizer) - 텍스트를 토큰 단위로 분할하는 도구
- **토큰** (Token) - 모델이 처리하는 최소 텍스트 단위
- **벡터 검색** (Vector Search) - 임베딩 벡터 간 유사도 기반 검색
- **시맨틱 검색** (Semantic Search) - 의미 기반 검색
- **파이프라인** (Pipeline) - 여러 처리 단계를 연결한 워크플로우

## 프레임워크 및 도구

### Hugging Face 생태계
- **허깅페이스** (Hugging Face) - 오픈소스 ML 플랫폼 및 라이브러리 제공업체
- **트랜스포머스** (Transformers) - Hugging Face의 핵심 라이브러리
- **데이터셋** (Datasets) - ML 데이터셋 처리 라이브러리
- **허브** (Hub) - 사전 훈련된 모델들의 저장소

### 개발 환경
- **주피터 노트북** (Jupyter Notebook) - 대화형 개발 환경
- **코랩** (Google Colab) - 구글의 클라우드 기반 노트북 환경
- **GPU** (Graphics Processing Unit) - 그래픽 처리 장치, ML 연산 가속화
- **CPU** (Central Processing Unit) - 중앙 처리 장치
- **MPS** (Metal Performance Shaders) - Apple Silicon Mac의 GPU 가속

## 특화 라이브러리

### 벡터 및 검색
- **FAISS** (Facebook AI Similarity Search) - 고속 벡터 유사도 검색 라이브러리
- **임베딩 모델** (Embedding Model) - 텍스트를 벡터로 변환하는 모델

### 토픽 모델링
- **BERTopic** - BERT 기반 토픽 모델링 라이브러리
- **토픽 모델링** (Topic Modeling) - 문서 집합에서 숨겨진 주제를 발견하는 기법
- **클러스터링** (Clustering) - 유사한 데이터를 그룹화하는 기법

### 강화학습
- **TRL** (Transformer Reinforcement Learning) - 트랜스포머 모델의 강화학습 라이브러리
- **PPO** (Proximal Policy Optimization) - 정책 최적화 알고리즘
- **보상 모델** (Reward Model) - 행동의 품질을 평가하는 모델

### API 및 통합
- **Cohere** - 상용 LLM API 서비스
- **LangChain** - LLM 애플리케이션 개발 프레임워크
- **OpenAI API** - OpenAI의 GPT 모델 API

## 평가 및 메트릭

### 성능 측정
- **SeqEval** - 시퀀스 라벨링 평가 도구
- **벤치마크** (Benchmark) - 모델 성능을 측정하는 표준 데이터셋
- **메트릭** (Metric) - 모델 성능을 수치화하는 지표

## 하드웨어 및 환경

### 컴퓨팅 환경
- **디바이스 설정** (Device Configuration) - 모델 실행 환경 지정
- **CUDA** - NVIDIA GPU 연산 플랫폼
- **배치 크기** (Batch Size) - 한 번에 처리하는 데이터 샘플 수
- **메모리 사용량** (Memory Usage) - 모델 실행에 필요한 RAM/VRAM

## 개발 도구

### 패키지 관리
- **uv** - 고속 Python 패키지 관리 도구
- **pyproject.toml** - Python 프로젝트 설정 파일
- **의존성** (Dependencies) - 프로젝트에 필요한 외부 라이브러리들
- **가상환경** (Virtual Environment) - 독립적인 Python 실행 환경

### 버전 관리
- **고정 버전** (Pinned Version) - 특정 버전으로 고정된 패키지
- **호환성** (Compatibility) - 다른 구성요소들과의 상호 운용성
- **잠금 파일** (Lock File) - 정확한 의존성 버전을 기록한 파일 (uv.lock)

---

## 약어 정리

| 약어 | 전체 이름 | 한국어 |
|------|-----------|--------|
| AI | Artificial Intelligence | 인공지능 |
| ML | Machine Learning | 머신러닝 |
| DL | Deep Learning | 딥러닝 |
| LLM | Large Language Model | 대규모 언어 모델 |
| NLP | Natural Language Processing | 자연어 처리 |
| GPU | Graphics Processing Unit | 그래픽 처리 장치 |
| CPU | Central Processing Unit | 중앙 처리 장치 |
| API | Application Programming Interface | 응용 프로그램 인터페이스 |
| RLHF | Reinforcement Learning from Human Feedback | 인간 피드백 강화학습 |
| PPO | Proximal Policy Optimization | 근접 정책 최적화 |
| FAISS | Facebook AI Similarity Search | 페이스북 AI 유사도 검색 |
| TRL | Transformer Reinforcement Learning | 트랜스포머 강화학습 |
| MPS | Metal Performance Shaders | 메탈 성능 셰이더 |

---

이 용어사전은 프로젝트 진행 중 새로운 용어가 추가되면 계속 업데이트됩니다.