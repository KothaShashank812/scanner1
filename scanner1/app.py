import streamlit as st

# Page setup
st.set_page_config(page_title="ShadowGuard Scanner", layout="wide")

st.title("🛡️ ShadowGuard Scanner")

# Read and display your HTML
with open("scanner1/scanner.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render the HTML
st.components.v1.html(html_content, height=900, scrolling=True)


