import streamlit as st

def home():
    st.title("Welcome to BruvCode Website!")
    st.write("Explore my Python tutorials and resources.")
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title(":mailbox: Find me here...")
        st.write("##")
        st.write("[🐈‍⬛GitHub >](https://github.com/Federico0965)")
        st.write("[💎Join my Discord server >](https://discord.gg/ccnCAXCe)")
        st.write("[🐦X (Formerly Twitter) >](https://x.com/FedericoBruv56)")
        st.write("[📹YouTube Channel (Python Channel) >](https://www.youtube.com/@BruvCode?sub_confirmation=1)")
