import streamlit as st
from streamlit_navigation_bar import st_navbar
import about, home, basics, advanced, projects

st.set_page_config(
    page_title="BruvCode - Master Python Programming",
    layout="wide"
)

def main_app():
    selected = st_navbar(pages=["Home", "About", "Basic Tutorials", "Advanced Tutorials", "Python Projects"])
    if selected == "Home":
        home.home()
    if selected == "About":
        about.about_me()
    if selected == "Basic Tutorials":
        basics.basics()
    if selected == "Advanced Tutorials":
        advanced.advanced()
    if selected == "Python Projects":
        projects.projects()

main_app()