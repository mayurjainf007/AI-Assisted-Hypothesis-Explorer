import os
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="AI-Assisted Hypothesis Explorer", layout="wide")
st.title("AI-Assisted Hypothesis Explorer")
st.write("Upload a CSV and ask a biological research question.")

api_url = os.getenv("API_URL", "http://localhost:8000")

with st.sidebar:
    st.header("Settings")
    api_url = st.text_input("Backend API URL", api_url)

uploaded = st.file_uploader("Upload CSV", type=["csv"])
question = st.text_input("Research question", value="What trends are associated with treatment response?")

if st.button("Summarize") and uploaded and question:
    files = {"file": (uploaded.name, uploaded.getvalue(), "text/csv")}
    data = {"question": question}
    try:
        r = requests.post(f"{api_url}/summarize", files=files, data=data, timeout=120)
        if r.ok:
            st.subheader("Summary")
            st.write(r.json().get("summary","<no summary>"))
        else:
            st.error(f"Backend error: {r.status_code} - {r.text}")
    except Exception as e:
        st.error(f"Failed to reach backend: {e}")

st.markdown("---")
st.subheader("Preview of CSV")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head(25))
