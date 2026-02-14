from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import pandas as pd
import torch
from .config import SETTINGS

from .text_utils import build_item_text, split_sentences
from .embeddings import encode_texts, cosine_sim



@dataclass
class PreparedCorpora:
    items_text: list[str]
    designers_text: list[str]



def build_corpora(df: pd.DataFrame, designer_df: pd.DataFrame | None = None) -> PreparedCorpora:
    """Build text corpora for items and designers."""

    items_text = []
    for product_name, material_pattern, colour, garment_group_name, clothing_description in zip(
            df["product_name"].tolist(),
            df["material_pattern"].tolist(),
            df["colour"].tolist(),
            df["garment_group_name"].tolist(),
            df["clothing_description"].tolist(),
    ):
        items_text.append(
            build_item_text(product_name, material_pattern, colour, garment_group_name, clothing_description)
        )

    if designer_df is not None:
        designers_text = [
            f"{name}: {desc}"
            for name, desc in zip(designer_df.index.tolist(), designer_df["Description"].tolist())
        ]
        return PreparedCorpora(items_text=items_text, designers_text=designers_text)

    return PreparedCorpora(items_text=items_text, designers_text=[])


def attach_compatible_designers(
        df: pd.DataFrame,
        item_emb,
        designer_emb,
        designer_names: pd.Index,
        top_k_designers: int = 6,
) -> pd.DataFrame:
    """Compute item->designer similarities and store sorted tuples in df['Compatible_designers']."""

    if isinstance(item_emb, torch.Tensor) and isinstance(designer_emb, torch.Tensor):
        sim = torch.matmul(item_emb, designer_emb.T)
        sim_np = sim.cpu().numpy()
    else:
        sim_np = np.asarray(item_emb) @ np.asarray(designer_emb).T

    out = df.copy()
    out["Compatible_designers"] = None

    for i in range(sim_np.shape[0]):
        row_scores = sim_np[i]
        idx = np.argsort(-row_scores)[:top_k_designers]
        out.at[i, "Compatible_designers"] = [(designer_names[j], float(row_scores[j])) for j in idx]

    return out


def recommend_from_query(
        user_query: str,
        df_with_designers: pd.DataFrame,
        item_emb,
        model_name: str = SETTINGS.model_name,
        top_k_items: int = 5,
        top_k_designers_per_item: int = 6,
) -> dict:
    """
    Recommend top items for a query, and aggregate designers from those items.
    Expects df_with_designers to have 'Compatible_designers' column already.
    """
    sentences = split_sentences(user_query)
    if not sentences:
        sentences = [user_query.strip()] if user_query.strip() else []

    if not sentences:
        return {"items": [], "designers": []}


    sent_emb = encode_texts(sentences, model_name=model_name, batch_size=16, to_tensor=True, normalize=True)
    if isinstance(sent_emb, torch.Tensor):
        query_emb = sent_emb.mean(dim=0)
    else:
        query_emb = sent_emb.mean(axis=0)


    sims = cosine_sim(query_emb, item_emb)
    if isinstance(sims, torch.Tensor):
        scores, indices = torch.topk(sims, k=min(top_k_items, sims.shape[0]))
        indices = indices.tolist()
        scores = scores.tolist()
    else:
        k = min(top_k_items, len(sims))
        indices = np.argsort(-sims)[:k].tolist()
        scores = [float(sims[i]) for i in indices]


    items = []
    designer_score_acc = {}

    for idx, sc in zip(indices, scores):
        row = df_with_designers.iloc[int(idx)]
        items.append(
            {
                "row_index": int(idx),
                "score": float(sc),
                "product_name": row.get("product_name"),
                "garment_group_name": row.get("garment_group_name"),
                "colour": row.get("colour"),
                "material_pattern": row.get("material_pattern"),
                "description": row.get("clothing_description"),
                "top_designers": (row.get("Compatible_designers") or [])[:top_k_designers_per_item],
            }
        )

        for dname, dscore in (row.get("Compatible_designers") or [])[:top_k_designers_per_item]:
            designer_score_acc[dname] = designer_score_acc.get(dname, 0.0) + float(dscore)

    designers_ranked = sorted(designer_score_acc.items(), key=lambda x: x[1], reverse=True)

    return {"items": items, "designers": designers_ranked}