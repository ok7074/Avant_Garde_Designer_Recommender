import streamlit as st
from Controller.ControllerImpl import ControllerImpl

# session state variables
if "clicked" not in st.session_state:
    st.session_state.clicked = False

if "recommended_designers" not in st.session_state:
    st.session_state.recommended_designers = []

# caching controller
@st.cache_data
def get_controller():
    return ControllerImpl()

controller = get_controller()

# page navigations
app_page = st.Page("app2.py", title="Home Page")
recommendations_page = st.Page("recommendation.py", title="Your Recommendations")

pg = st.navigation([app_page, recommendations_page])

st.title("Avant Garde Designer Recommender")

# creating a stateful button
button_col, input_col = st.columns(2)

def set_click_and_query():
    st.session_state.clicked = True

input_col.text_input(
    "Please enter your description here:",
    key="user_query"
)

button_col.button(
    "Generate recommendation",
    on_click=set_click_and_query
)

if st.session_state.clicked:
    st.session_state.recommended_designers = controller.make_recommendation(
        st.session_state.user_query
    )

st.write(st.session_state.recommended_designers)
