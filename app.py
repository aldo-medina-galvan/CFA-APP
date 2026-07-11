from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="CFA Level I Study App",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default chrome so the embedded study app uses the full page.
st.markdown(
    """
    <style>
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        footer {
            display: none;
        }

        .block-container {
            max-width: 100%;
            padding: 0;
        }

        iframe {
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).with_name("study_app.html")
html_content = html_path.read_text(encoding="utf-8")

# The original HTML contains its own CSS, JavaScript, local progress storage,
# Daily Review, Mistake Book, dashboard, and import/export functions.
components.html(
    html_content,
    height=1450,
    scrolling=True,
)
