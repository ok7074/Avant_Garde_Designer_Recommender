import streamlit as streamlit
import streamlit.components.v1 as components
from .ControllerImpl import ControllerImpl
from .embeddings import get_model
from .config import SETTINGS

#caching data
controller = ControllerImpl()
@st.cache_data
df= controller.data_prep_and_embed()
#replace model_name parameter in all src packages so it doesnt need to be entered again



#page navigations
app_page= st.Page("app2.py", title= "Home Page")
recommendations_page= st.Page("recommendation.py", title="Your Recommendations")

pg = st.navigation([app_page,recommendations_page])
st.title("Avant Garde Designer Recommender")



#creating a stateful button
if "clicked" not in st.session_state:
    st.session_state.clicked=False


button_col, input_col= st.columns(2)

def set_click_and_query():
    st.session_state.clicked=True


input_col.text_input("Please enter your description here:", key="user_query")
button_col.button("Generate recommendation", on_click=set_click)


if st.session_state.clicked:
    recommendations=controller.generate_recommendation(st.session_state.user_query, df)
        



    



st.write()






# two containers have been created and part of the controller logic is done. 