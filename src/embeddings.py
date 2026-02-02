from __future__ import annotations

from functools import lru_cache
import numpy as np
from sentence_transformers import SentenceTransformer
import torch

@lru_cache(maxsize=1)
def get_model(model_name: str) -> SentenceTransformer:
    """Load SBERT model once per process."""
    return SentenceTransformer(model_name)

def encode_texts(
    texts: list[str],
    model_name: str,
    batch_size: int = 32,
    to_tensor: bool = True,
    normalize: bool = True,
):
    """Encode a list of texts into embeddings."""
    model = get_model(model_name)
    emb = model.encode(
        texts,
        batch_size=batch_size,
        convert_to_tensor=to_tensor,
        normalize_embeddings=normalize,
        show_progress_bar=False,
    )
    return emb

def cosine_sim(query_emb, corpus_emb):
    """Cosine similarity. If embeddings are normalized, this is just dot product."""
    if isinstance(query_emb, torch.Tensor) and isinstance(corpus_emb, torch.Tensor):
        # (d,) @ (n,d)^T => (n,)
        return torch.matmul(corpus_emb, query_emb)
    # numpy fallback
    q = np.asarray(query_emb)
    c = np.asarray(corpus_emb)
    return c @ q
