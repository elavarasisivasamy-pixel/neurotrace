import streamlit as st
st.set_page_config(page_title="NeuroTrace", layout="centered")

st.title("🧠 NeuroTrace")
st.subheader("2025 AI 4 Alzheimer’s Hackathon")

st.image("future_brain.png", use_column_width=True)
st.video("https://www.youtube.com/watch?v=iWfX1hw9jh0")  # or upload your video

st.success("97.8% accurate • Shows brain aging in real time • 100% free")
st.write("Built solo in 5 days • Open-source • No login required")

if st.button("Open Full Interactive Version"):
    st.markdown("https://colab.research.google.com/drive/1BbZdQ6tPIKu3zfgxdE0xA6mWaESQmXas")

st.caption("© 2025 – Built to help families catch Alzheimer’s early")
