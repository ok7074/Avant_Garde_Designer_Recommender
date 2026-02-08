import streamlit as streamlit
import streamlit.components.v1 as components


components.html(
    """
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Designer One</title>
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
                        {st.session_state.recommended_designers[0]}
                    </h1>
                </div>
                
                <!-- Column 2: Article Text -->
                <div class="col-lg-6 col-md-5 col-6 mb-4">
                    <div class="article-text">
                        <h2>
                            <strong>{st.session_state.recommended_designers[0]}</strong> 
                        </h2>
                        
                        <p>
                            {st.controller.write_article_text(st.session_state.recommended_designers[0])}
                        </p>
                    </div>
                </div>
                
                <!-- Column 3: Images -->
                <div class="col-lg-4 col-md-4 col-12">
                    <div class="image-column">
                        <!-- Main featured image -->
                        <img src= st.session_state.images[0][0]
                             alt="Featured image" 
                             class="main-image">
                        
                        <!-- Additional images can be added below -->
                        <!-- <img src="your-image-url.jpg" alt="Additional image"> -->
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    """,
    height=600
)