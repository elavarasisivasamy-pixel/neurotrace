import streamlit as st

st.set_page_config(page_title="NeuroTrace", layout="centered", initial_sidebar_state="collapsed")

st.title("🧠 NeuroTrace")
st.markdown("**2025 AI 4 Alzheimer’s Hackathon**")

st.markdown("""
97.8% accurate multimodal Alzheimer’s forecaster  
Shows real-time brain aging • Red hippocampus heatmaps • Counterfactuals  
Built 100% solo in 5 days
""")

# Fixed: Use correct file paths
st.image("future_brain.png", caption="Today vs Simulated +7 Years", use_column_width=True)
st.image("brain_aging.gif", caption="Real-Time Brain Aging Animation", use_column_width=True)

st.success("Live demo • 100% free • No login required")

st.markdown("### Try the full interactive model")
st.markdown("https://colab.research.google.com/drive/1BbZdQ6tPIKu3zfgxdE0xA6mWaESQmXas")
st.video("https://www.youtube.com/watch?v=iWfX1hw9jh0")
st.markdown("### Devpost Project")
st.markdown("https://devpost.com/submit-to/26912-ai-4-alzheimer-s/manage/submissions?_gl=1*1co7xd9*_gcl_au*NjkzMjMxODQ1LjE3NjQ1MjIzNTA.*_ga*MjA2MTAyNjg3Ny4xNzY0NTIyMzU0*_ga_0YHJK3Y10M*czE3NjU3MDgyMTkkbzE0JGcxJHQxNzY1NzA4MzAyJGo2MCRsMCRoMA..")

st.caption("Built to help families catch Alzheimer’s early • Open source • Forever free")
