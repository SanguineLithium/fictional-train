# Ethical AI/ML Template — Neil Goldstein

**AI-assisted, human-reviewed.**
This template shows how I use GenAI to accelerate the boring parts while keeping humans in charge of quality.

## What's here
- **Synthetic data** only (safe to share)
- **Labelled** AI assistance (see /ethics/AI_ASSIST_DISCLOSURE.md)
- **Reproducible** notebook and pipeline
- **Tests** and a **review checklist**

## Quickstart (Windows)

    python -m venv .venv
    . .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python scripts\generate_synthetic_data.py
    pytest
    jupyter lab

## Principles
1. Automate scaffolds; humans own decisions.
2. Label AI involvement.
3. Test before you trust.
4. Prefer synthetic/redacted data for sharing.
