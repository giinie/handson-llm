# Project Overview

## Purpose
이 프로젝트는 **핸즈온 LLM (한빛미디어, 2025)** 교재의 코드 실습 환경입니다. 12개 장으로 구성된 대규모 언어 모델(LLM) 학습서의 Jupyter 노트북 예제들을 포함합니다.

## Tech Stack
- **언어**: Python 3.13+
- **패키지 관리**: uv (pyproject.toml 기반)
- **주요 프레임워크**: 
  - transformers 4.48.3 (Hugging Face)
  - torch (PyTorch)
  - datasets
  - notebook (Jupyter)
- **ML/AI 라이브러리**: 
  - faiss-cpu (벡터 검색)
  - bertopic (토픽 모델링)
  - setfit (Few-shot 학습)
  - trl (강화 학습)
  - cohere (Cohere API)
  - langchain-openai & langchain-community

## Project Structure
```
handson-llm/
├── chapter01-12.ipynb    # 각 장별 실습 노트북
├── practice/             # 연습용 코드
│   ├── model.py         # 기본 모델 사용 예제
│   └── model.ipynb      # 노트북 형태의 연습
├── pyproject.toml       # 프로젝트 설정 및 의존성
├── uv.lock             # 의존성 잠금 파일
└── README.md           # 각 장별 GitHub/Colab 링크
```

## Development Environment
- **GPU 사용 권장**: 코랩에서 T4 GPU 사용 권장
- **디바이스 설정**: 
  - CPU: `device="cpu"` 또는 `device=-1`
  - Mac Apple GPU: `device="mps"`
  - CUDA GPU: `device=0` 또는 `device="cuda"`