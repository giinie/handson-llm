# 개발 가이드라인

## Code Style & Conventions
- **Python 표준**: PEP 8 준수
- **타입 힌트**: 사용 권장 (pandas-stubs 포함됨)
- **패키지 구조**: practice/ 디렉터리에서 실험적 코드 작성

## 노트북 개발 패턴
- **GPU 설정**: 코드 시작 전에 적절한 디바이스 설정
- **패키지 설치**: 노트북 내에서 `!pip install` 사용 시 버전 고정
- **한글 주석**: 교육 목적으로 한글 주석 사용
- **예제 코드**: practice/model.py처럼 간단한 예제부터 시작

## 디바이스 설정 가이드라인
```python
# Transformers pipeline 디바이스 설정 예제
pipe = pipeline("text-generation", model="model-name", device="cpu")  # CPU
pipe = pipeline("text-generation", model="model-name", device="mps")  # Mac GPU
pipe = pipeline("text-generation", model="model-name", device=0)      # CUDA GPU
```

## 의존성 관리
- **pyproject.toml** 사용하여 중앙 집중식 의존성 관리
- **버전 고정**: 호환성을 위해 주요 패키지 버전 고정 (예: transformers==4.48.3)
- **GPU 지원**: torch 설치 시 GPU 버전 고려

## 교육용 코드 특성
- **단계별 설명**: 각 단계마다 명확한 주석
- **에러 방지**: 초보자도 쉽게 따라할 수 있도록 명확한 설치 가이드
- **실무 연결**: 이론과 실습의 연결점 제공