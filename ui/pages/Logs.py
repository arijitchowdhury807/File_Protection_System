import streamlit as st
import os

st.set_page_config(
    page_title="Security Logs",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Security Logs")

st.divider()

log_file = "data/logs/security.log"

if os.path.exists(log_file):

    with open(log_file, "r") as f:

        logs = f.read()

    if logs.strip():

        st.code(
            logs,
            language="text"
        )

    else:

        st.info(
            "No log entries found."
        )

else:

    st.warning(
        "Log file not found."
    )