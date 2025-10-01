import sys, os
from pathlib import Path

# Add repo root to sys.path so "from src.pipeline import ..." works
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
