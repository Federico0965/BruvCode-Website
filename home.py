import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_designer = load_lottieurl("https://lottie.host/9a780094-8507-44b0-a981-4ae68b94cead/vLLZAlCNgl.json")
lottie_video = load_lottieurl("https://lottie.host/c70af8c5-b889-436e-ade1-f578a54da4bb/8GMGLpzHHI.json")

def home():
    st.title("Welcome to BruvCode Website!")
    st.write("Explore my Python tutorials and resources.")
    st_lottie(lottie_designer, height=300, key="designer")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title(":mailbox: Find me here...")
        st.write("##")
        st.write("[🐈‍⬛GitHub >](https://github.com/Federico0965)")
        st.write("[💎Join my Discord server >](https://discord.gg/ccnCAXCe)")
        st.write("[🐦X (Formerly Twitter) >](https://x.com/FedericoBruv56)")
        st.write("[📹YouTube Channel (Python Channel) >](https://www.youtube.com/@BruvCode?sub_confirmation=1)")
    with right_column:
        st_lottie(lottie_video, height=300, key="video")