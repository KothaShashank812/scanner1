import streamlit as st

# Set page title and layout
st.set_page_config(page_title="ShadowGuard Scanner", layout="wide")

# Read your HTML file
with open("scanner.html", "r", encoding="utf-8") as file:
    html_code = file.read()

# Display HTML inside an iframe
st.components.v1.html(html_code, height=900, scrolling=True)
