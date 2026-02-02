# Private Project (Streamlit)

This repo is a clean skeleton for your Streamlit app + a reusable Python "backend" in `src/`.

## Quickstart

1) Create and activate a virtual environment  
2) Install deps:
```bash
pip install -r requirements.txt
```

3) Run:
```bash
streamlit run app.py
```

## Folder structure

- `app.py` — Streamlit UI (keep it thin)
- `src/` — all core logic (data loading, preprocessing, embeddings, similarity, recommenders)
- `notebooks/` — experiments (kept for reference)
- `data/` — place your data locally (do not commit big datasets)
- `assets/` — CSS, images
- `.streamlit/` — Streamlit config and secrets example

## Data

Put your full dataset under `data/raw/` locally (gitignored).
Optionally keep a tiny sample in `data/sample/` for testing.
