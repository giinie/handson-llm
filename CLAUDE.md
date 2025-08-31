# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Korean educational repository for **"핸즈온 LLM" (Hands-on LLM, Hanbit Media, 2025)**. It contains 12 Jupyter notebooks (chapter01-12.ipynb) that demonstrate various Large Language Model techniques and implementations.

## Development Environment & Setup

### Package Management
This project uses **uv** for dependency management with `pyproject.toml` configuration.

```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate

# Add new packages
uv add <package_name>
```

### Key Dependencies
- **transformers==4.48.3** (version pinned for Phi-3 model compatibility)
- **torch** (PyTorch for deep learning)
- **notebook** (Jupyter environment)
- **datasets**, **faiss-cpu**, **bertopic**, **setfit**, **trl** (ML/AI libraries)
- **langchain-openai**, **cohere** (LLM integration)

### Python Environment
- Requires **Python 3.13+**
- Virtual environment managed by uv (`.venv/`)

## Common Development Commands

### Running Notebooks
```bash
# Start Jupyter Notebook
jupyter notebook
# or with uv
uv run jupyter notebook

# For external access
jupyter notebook --ip=0.0.0.0 --port=8888
```

### Python Execution
```bash
# Run Python scripts
python practice/model.py
# or with uv
uv run python practice/model.py
```

### GPU/Device Configuration
The notebooks are designed to work with different compute environments:
- **CPU**: `device="cpu"` or `device=-1`
- **Mac Apple GPU**: `device="mps"`
- **CUDA GPU**: `device=0` or `device="cuda"`

## Code Architecture & Structure

### Repository Layout
```
handson-llm/
├── chapter01-12.ipynb    # Educational notebooks for each chapter
├── practice/             # Practice and example code
│   ├── model.py         # Basic transformer usage example
│   └── model.ipynb      # Notebook version of examples
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Dependency lock file
└── README.md           # Links to GitHub and Colab versions
```

### Key Patterns
- **Educational Focus**: Korean comments and explanations for learning
- **Device Flexibility**: Code examples show CPU/GPU/MPS configurations
- **Transformers Pipeline**: Primary pattern using Hugging Face transformers
- **Step-by-Step Examples**: Each notebook builds concepts progressively

### Example Code Pattern
```python
from transformers import pipeline

# Create pipeline with explicit device setting
pipe = pipeline("text-generation", model="openai-community/gpt2", device="cpu")
result = pipe("Your prompt here", max_new_tokens=200)
print(result)
```

## Working with This Codebase

### When Adding New Code
1. Use the `practice/` directory for experimental code
2. Follow the device configuration patterns shown in existing examples
3. Add Korean comments for educational clarity
4. Test on both CPU and GPU if possible

### Notebook Development
- **GPU Recommendation**: Notebooks suggest using T4 GPU in Google Colab
- **Installation Pattern**: Use `!pip install package==version` in notebooks when needed
- **Educational Structure**: Each chapter builds on previous concepts
- **Colab Compatibility**: All notebooks should work in Google Colab environment

### Quality Assurance
- Test notebooks by running all cells sequentially
- Verify device settings work for target environment
- Ensure new dependencies are added to `pyproject.toml`
- Check compatibility with Google Colab for educational use

### No Traditional Development Tools
- **No linting configuration** (educational project)
- **No automated testing** (manual notebook execution for validation)
- **No CI/CD** (simple educational repository)
- **No pre-commit hooks** (keep setup simple for learners)