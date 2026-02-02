import streamlit as st
import pandas as pd

from src.config import SETTINGS
from src.preprocess import preprocess_articles
from src.designer_dna import make_designer_df
from src.embeddings import encode_texts
from src.recommender import build_corpora, attach_compatible_designers, recommend_from_query

st.set_page_config(page_title="Private Project", layout="wide")

# --- Optional: super simple password gate (uses Streamlit secrets) ---
APP_PASSWORD = st.secrets.get("APP_PASSWORD", None)
if APP_PASSWORD:
    if "authed" not in st.session_state:
        st.session_state.authed = False

    if not st.session_state.authed:
        st.title("🔒 Private App")
        pwd = st.text_input("Password", type="password")
        if st.button("Enter"):
            if pwd == APP_PASSWORD:
                st.session_state.authed = True
                st.rerun()
            else:
                st.error("Wrong password")
        st.stop()

st.title("✨ Private Project (Placeholder)")
st.caption("Streamlit UI kept thin. Core logic lives in src/.")

with st.sidebar:
    st.header("Settings")
    articles_path = st.text_input("Articles CSV path", value=SETTINGS.articles_csv_path)
    top_k_items = st.number_input("Top items", min_value=1, max_value=50, value=SETTINGS.top_k_items)
    top_k_designers = st.number_input("Top designers per item", min_value=1, max_value=50, value=SETTINGS.top_k_designers)
    model_name = st.text_input("Embedding model", value=SETTINGS.model_name)
    st.divider()
    load_btn = st.button("Load + Prepare", use_container_width=True)

@st.cache_data(show_spinner=False)
def _load_and_preprocess(path: str) -> pd.DataFrame:
    raw = pd.read_csv(path)
    return preprocess_articles(raw)

@st.cache_resource(show_spinner=False)
def _prepare_embeddings(df: pd.DataFrame, model_name: str):
    designer_df = make_designer_df()
    corpora = build_corpora(df, designer_df)

    item_emb = encode_texts(corpora.items_text, model_name=model_name, batch_size=32, to_tensor=True, normalize=True)
    designer_emb = encode_texts(corpora.designers_text, model_name=model_name, batch_size=32, to_tensor=True, normalize=True)

    df_with_designers = attach_compatible_designers(
        df=df,
        item_emb=item_emb,
        designer_emb=designer_emb,
        designer_names=designer_df.index,
        top_k_designers=int(st.session_state.get("top_k_designers_cached", 6)),
    )
    return df_with_designers, item_emb

if load_btn:
    try:
        st.session_state["df"] = _load_and_preprocess(articles_path)
        st.session_state["top_k_designers_cached"] = int(top_k_designers)
        st.success(f"Loaded and cleaned: {len(st.session_state['df'])} rows")
    except Exception as e:
        st.error(f"Failed to load data: {e}")

if "df" not in st.session_state:
    st.info("Set your dataset path in the sidebar and click **Load + Prepare**.")
    st.stop()

df = st.session_state["df"]

st.subheader("Dataset preview")
st.dataframe(df.head(20), use_container_width=True)

st.divider()
st.subheader("Query")
user_query = st.text_input("Describe what you're looking for", placeholder="e.g., black draped leather, brutalist silhouettes, heavy boots...")

colA, colB = st.columns([1,1])
with colA:
    run = st.button("Recommend", use_container_width=True)
with colB:
    show_rows = st.checkbox("Show matched item rows", value=True)

if run:
    with st.spinner("Preparing embeddings (first run can take a moment)..."):
        df_with_designers, item_emb = _prepare_embeddings(df, model_name)

    rec = recommend_from_query(
        user_query=user_query,
        model_name=model_name,
        df_with_designers=df_with_designers,
        item_emb=item_emb,
        top_k_items=int(top_k_items),
        top_k_designers_per_item=int(top_k_designers),
    )

    st.markdown("### Top designers (aggregated)")
    if rec["designers"]:
        st.write(rec["designers"][:20])
    else:
        st.write("No designers found (empty query?).")

    st.markdown("### Top items")
    for item in rec["items"]:
        with st.container(border=True):
            st.write(f"**Score:** {item['score']:.4f}")
            st.write(f"**{item['product_name']}** — {item['garment_group_name']} — {item['colour']} — {item['material_pattern']}")
            st.write(item["description"])
            st.write("**Top designers for this item:**")
            st.write(item["top_designers"])

            if show_rows:
                st.caption(f"Row index in cleaned df: {item['row_index']}")
