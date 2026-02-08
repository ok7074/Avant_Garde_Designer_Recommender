from __future__ import annotations

import numpy as np
import pandas as pd

def get_value_from_description(row: pd.Series, garments_set: set[str]) -> pd.Series:
    """Fill missing garment_group_name by checking if any existing garment token appears in description."""
    if pd.isna(row.get("garment_group_name")):
        desc = str(row.get("clothing_description") or "")
        if desc != "no description given":
            words = set(desc.lower().split())
            hit = next((g for g in garments_set if g in words), None)
            row["garment_group_name"] = hit if hit else "no garment type provided"
        else:
            row["garment_group_name"] = "no garment type provided"
    return row

def preprocess_articles(raw_df: pd.DataFrame) -> pd.DataFrame:
    """Replicates the cleaning steps from the notebook in a reusable function."""
    df = raw_df.copy()

    # Keep only object columns (as in notebook)
    df = df.select_dtypes(include=["object"]).copy()

    # Drop columns you removed in the notebook (ignore if missing)
    df = df.drop(
        columns=[
            "index_code",
            "index_group_name",
            "prod_name",
            "perceived_colour_value_name",
            "perceived_colour_master_name",
        ],
        errors="ignore",
    )
    df = df.drop(columns=["department_name", "index_name", "section_name"], errors="ignore")

    # Merge product_group_name into garment_group_name for low-signal values
    unwanted_values_garment = ["Special Offers", "Unknown"]
    unwanted_values_product = ["Items", "Unknown", "Fun"]

    if "garment_group_name" in df.columns and "product_group_name" in df.columns:
        df["garment_group_name"] = df["garment_group_name"].replace(unwanted_values_garment, np.nan).fillna(
            df["product_group_name"].replace(unwanted_values_product, np.nan)
        )

    df = df.drop(columns=["product_group_name"], errors="ignore")

    # Rename columns to your normalized names
    new_names_columns = {
        "product_type_name": "product_name",
        "graphical_appearance_name": "material_pattern",
        "detail_desc": "clothing_description",
        "colour_group_name": "colour",
    }
    df = df.rename(columns=new_names_columns)

    # Basic cleanup
    if "clothing_description" in df.columns:
        df["clothing_description"] = df["clothing_description"].fillna("no description given")

    df = df.drop_duplicates()

    # Fill garment group from description when missing
    if "garment_group_name" in df.columns and "clothing_description" in df.columns:
        garments_set = set(df["garment_group_name"].dropna().astype(str).str.lower().unique())
        df = df.apply(get_value_from_description, axis=1, garments_set=garments_set)

    # Remove unwanted product categories (copied from notebook; fixed formatting for safety)
    unwanted_categories = [
        "Hair clip","Umbrella","Hair string","Sleep Bag","Swimwear bottom","Underwear bottom","Swimsuit","Kids Underwear top",
        "Alice band","Straw hat","Giftbox","Sleeping sack","Wallet","Swimwear set","Swimwear top","Waterbottle","Fine cosmetics",
        "Nipple covers","Chem. cosmetics","Soft Toys","Hair ties","Bra extender","Blanket","Hairband","Side table","Keychain",
        "Dog Wear","Washing bag","Sewing kit","Towel","Wood balls","Bumbag","Dog wear","Wireless earphone case",
        "Stain remover spray","Clothing mist","Baby Bib","Mobile case","Pre-walkers","Toy"
    ]
    if "product_name" in df.columns:
        df = df[~df["product_name"].isin(unwanted_categories)]

    unwanted_garments = ["Swimwear", "Woven/Jersey/Knitted mix Baby", "Stationery"]
    if "garment_group_name" in df.columns:
        df = df[~df["garment_group_name"].isin(unwanted_garments)]

    return df.reset_index(drop=True)
