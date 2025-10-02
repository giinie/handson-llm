# AGENTS.md - Agent Development Guide

## Project Overview
Educational repository for "핸즈온 LLM" (Hands-on LLM, Hanbit Media, 2025). Contains 12 Jupyter notebooks demonstrating LLM techniques, plus RAG implementation in `rag/`.

## Environment & Setup
- **Python:** 3.13+ required
- **Package Manager:** uv (`uv sync` to install dependencies, `uv add <pkg>` to add new ones)
- **Activate venv:** `source .venv/bin/activate`

## Common Commands
- **Start Jupyter:** `jupyter notebook` or `uv run jupyter notebook`
- **Run Python scripts:** `python practice/model.py` or `uv run python <script>`
- **RAG pipeline:** `python rag/ingest.py` (build corpus), then `python rag/qa.py` (query)
- **No formal linting/testing:** This is an educational project—validate by running notebooks end-to-end

## Architecture
- `chapter01-12.ipynb`: Educational notebooks for each chapter
- `rag/`: RAG implementation (ingest.py, search.py, qa.py with BM25 + FAISS hybrid search)
- `practice/`: Practice code and examples
- `pyproject.toml`: Dependencies with pinned versions (transformers==4.48.3 for Phi-3 compatibility)

## Code Style & Conventions
- **Educational focus:** Add Korean comments for clarity
- **Device flexibility:** Use `device="cpu"`, `device="mps"` (Mac GPU), or `device=0` (CUDA)
- **Transformers pattern:** Primary pattern is `pipeline()` from Hugging Face
- **Colab compatibility:** All notebooks must work in Google Colab (recommend T4 GPU)
- **Dependencies:** Always add new packages to `pyproject.toml`
- **No strict linting/testing:** Keep setup simple for learners
