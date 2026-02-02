from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    # Model
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Ranking
    top_k_items: int = 5
    top_k_designers: int = 6

    # Data paths (edit to match your local setup)
    articles_csv_path: str = "data/raw/articles.csv"

SETTINGS = Settings()
