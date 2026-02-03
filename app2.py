import streamlit as streamlit
import streamlit.components.v1 as components

st.title("Avant Garde Designer Recommender")

components.html(
    """
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
    <div class="container-fluid">
        <div class="container text-center">
            <div class="row">
                <div class="col">
                Text Col
                </div>
                <div class="col">
                picture col
                </div>
            </div>
        </div>
    </div>
    """,
    height=600
)

# two containers have been created and part of the controller logic is done. 