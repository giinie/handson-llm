# SuperGemini Onboarding

This document provides a comprehensive overview of the **handson-llm** project, designed to serve as a quick-start guide for AI agents.

## Project Overview

This project is the official code repository for the book **"<핸즈온 LLM>(한빛미디어, 2025)"**. It contains Jupyter notebooks for each of the 12 chapters, providing hands-on examples for learning about Large Language Models (LLMs).

The project is structured as a collection of notebooks and Python scripts that demonstrate various LLM concepts, including:
*   Text generation with pre-trained models (GPT-2).
*   Retrieval-Augmented Generation (RAG) with a hybrid search implementation.
*   Topic modeling with BERTopic.
*   Few-shot learning with SetFit.
*   Reinforcement learning with TRL.

### Tech Stack

*   **Language:** Python 3.13+
*   **Package Manager:** uv
*   **Core Frameworks:**
    *   `transformers`
    *   `torch`
    *   `langchain`
    *   `jupyter`
*   **Key Libraries:**
    *   `faiss-cpu`: For efficient similarity search.
    *   `bertopic`: For topic modeling.
    *   `setfit`: For few-shot learning.
    *   `trl`: For reinforcement learning.
    *   `cohere`: For using the Cohere API.

## Building and Running

### 1. Setup Environment

It is recommended to use a virtual environment.

```bash
# Install dependencies using uv
uv pip install -r requirements.txt
```
*Note: A `requirements.txt` file can be generated from `pyproject.toml` or `uv.lock`.*

### 2. Running Jupyter Notebooks

The primary way to interact with this project is through the Jupyter notebooks.

```bash
# Start the Jupyter Notebook server
jupyter notebook
```

Then, open the notebook for the desired chapter in your browser.

### 3. Running the RAG Pipeline

The `rag` directory contains a simple RAG implementation.

```bash
# 1. Ingest data into the corpus
python rag/ingest.py

# 2. Run a query against the corpus
python rag/qa.py
```

## Development Conventions

*   **Code Style:** The project does not have a strict code style guide, but the existing code is well-structured and readable.
*   **CI/CD:** The project uses GitHub Actions with `anthropics/claude-code-action` for automated code reviews on pull requests. This indicates a commitment to code quality.
*   **AI-Assisted Development:** The presence of the `.serena` directory and `prompts` suggests that the project is developed with the assistance of AI agents. The `project_overview.md` in the `.serena/memories` directory is a good example of this.
*   **Testing:** There is no formal testing framework (`pytest`, etc.) in this project. This is an area for potential improvement.

## Key Files and Directories

*   `chapter*.ipynb`: Jupyter notebooks for each chapter of the book.
*   `rag/`: A simple Retrieval-Augmented Generation (RAG) implementation.
    *   `ingest.py`: Script to build the knowledge base.
    *   `search.py`: Implements the hybrid search (BM25 + FAISS).
    *   `qa.py`: Script to run a query against the knowledge base.
*   `practice/`: Directory for practice code and notebooks.
*   `pyproject.toml`: Defines project dependencies.
*   `GLOSSARY.md`: A comprehensive glossary of terms.
*   `.serena/memories/`: Contains memories for AI agents, such as the project overview.
*   `.github/workflows/`: Contains GitHub Actions workflows for CI/CD.
