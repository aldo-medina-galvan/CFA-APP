from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CFA Level I Study App", layout="wide")
html_content = Path(__file__).with_name("study_app.html").read_text(encoding="utf-8")
components.html(html_content, height=1450, scrolling=True)
