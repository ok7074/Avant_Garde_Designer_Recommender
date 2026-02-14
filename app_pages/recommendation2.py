import streamlit as st
import streamlit.components.v1 as components


if len(st.session_state.get("recommended_designers", [])) < 2:
    st.warning("Please go to the Home Page and generate a recommendation first.")
    st.stop()

designer_name = st.session_state.recommended_designers[1][0]  # designers_ranked is a list of (name, score) tuples


from src.code_packages.designer_dna import designer_dna
article_text = designer_dna.get(designer_name, "No description available.")

# Safely retrieve image URL — images is a dict keyed by designer name.
images_dict = st.session_state.get("images", {})
designer_images = images_dict.get(designer_name, [])
image_url = designer_images[0] if designer_images else ""


html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Designer Two</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container-fluid">
        <div class="magazine-container">
            <div class="row">
                <!-- Column 1: Big Bold Text -->
                <div class="col-lg-2 col-md-3 col-6 mb-4">
                    <h1 class="big-text">
                        {designer_name}
                    </h1>
                </div>

                <!-- Column 2: Article Text -->
                <div class="col-lg-6 col-md-5 col-6 mb-4">
                    <div class="article-text">
                        <h2>
                            <strong>{designer_name}</strong>
                        </h2>
                        <p>
                            {article_text}
                        </p>
                    </div>
                </div>

                <!-- Column 3: Images -->
                <div class="col-lg-4 col-md-4 col-12">
                    <div class="image-column">
                        <img src="{image_url}"
                             alt="Featured image"
                             class="main-image">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

components.html(html_content, height=600)