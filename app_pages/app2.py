import streamlit as st
import streamlit.components.v1 as components
from Controller.ControllerImpl import ControllerImpl
from src.embeddings import get_model
from src.config import SETTINGS

#session state variables
if "clicked" not in st.session_state:
    st.session_state.clicked=False

if "recommended_designers" not in st.session_state:
    st.session_state.recommended_designers=[]

#caching data
@st.cache_data
controller=ControllerImpl()


#page navigations
app_page= st.Page("app2.py", title= "Home Page")
recommendations_page= st.Page("recommendation.py", title="Your Recommendations")

pg = st.navigation([app_page,recommendations_page])
st.title("Avant Garde Designer Recommender")



#creating a stateful button
button_col, input_col= st.columns(2)

def set_click_and_query():
    st.session_state.clicked=True


input_col.text_input("Please enter your description here:", key="user_query")
button_col.button("Generate recommendation", on_click=set_click_and_query)


if st.session_state.clicked:
    st.session_state.recommended_designers=controller.make_recommendation(st.session_state.user_query, df)
        



    



st.write()






# two containers have been created and part of the controller logic is done. 