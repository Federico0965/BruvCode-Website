import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/924ecd9e-1512-4e6f-b21a-f696571d381b/pU6OJ1olFh.json")

def about_me():
    # ---- HEADER SECTION ----
    with st.container():
        st.subheader("Hi, I am Federico :wave:")
        st.title("A Python YouTuber, Coder, and Lecturer")
        st.write("I am passtionate about finding ways to use Python and RealPython to be more efficient and effective in business settings.")
        st.write("[Learn more about Python and RealPython >](https://www.realpython.com/)")
    
    # ---- WHAT I DO ----
    st.write("---")
    left_column, right_column = st.columns(2)
    with st.container():
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
                """
                On my YouTube channel, I am making tutorials for people who:
                - are finding ways to learn the Python Basics
                - are finding ways to create Python Projects
                - are finding ways to master the Intermediate OOP Programming with Python classes

                If this sounds interesting to you, consider subscribing and turning on notifications so you don't miss on any new easy-to-follow Python Tutorials
                """
            )
            st.write("[Subscribe here (Weekly uploads) >](https://rb.gy/9x4m89)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")