from __future__ import annotations

def split_sentences(text: str) -> list[str]:
    """Simple sentence split on '.' with cleanup."""
    if text is None:
        return []
    parts = [p.strip() for p in str(text).split(".")]
    return [p for p in parts if p]

def safe_str(x) -> str:
    return "" if x is None else str(x)

def build_item_text(
    product_name: str,
    material_pattern: str,
    colour: str,
    garment_group_name: str,
    clothing_description: str,
) -> str:
    """Create a single text string per clothing item (for embeddings)."""
    return (
        f"Product Name is {safe_str(product_name)}, "
        f"the material is a {safe_str(material_pattern)} of the colour {safe_str(colour)} "
        f"and belongs to the garment group {safe_str(garment_group_name)}. "
        f"The garment can be described as follows: {safe_str(clothing_description)}"
    )
