# 개발 명령어

## 환경 설정
```bash
# 프로젝트 의존성 설치
uv sync

# 가상환경 활성화
source .venv/bin/activate

# Jupyter 노트북 실행
jupyter notebook
# 또는
uv run jupyter notebook
```

## 패키지 관리
```bash
# 새 패키지 추가
uv add <package_name>

# 개발 의존성 추가
uv add --dev <package_name>

# 패키지 제거
uv remove <package_name>

# 의존성 업데이트
uv sync --upgrade
```

## Python 실행
```bash
# Python 스크립트 실행 (가상환경 내에서)
python practice/model.py
# 또는 uv를 통해
uv run python practice/model.py

# Python 인터프리터 (가상환경 내에서)
python
# 또는
uv run python
```

## 노트북 관리
```bash
# 특정 노트북을 코랩에서 열기
# GitHub 링크 사용: https://github.com/rickiepark/handson-llm/blob/main/chapter{N}.ipynb
# Colab 링크: https://colab.research.google.com/github/rickiepark/handson-llm/blob/main/chapter{N}.ipynb

# 노트북 서버 시작
jupyter notebook --ip=0.0.0.0 --port=8888

# Jupyter Lab 사용
jupyter lab
```

## 시스템 정보 확인
```bash
# Python 버전 확인
python --version

# UV 버전 확인
uv --version

# 설치된 패키지 목록
uv pip list
```