import streamlit as st
import os

st.set_page_config(
    page_title="Settings",
    page_icon="⚙",
    layout="wide"
)

st.title("⚙ System Settings")

st.divider()

# -------------------------
# Auto Recovery Setting
# -------------------------

st.subheader("♻ Recovery Settings")

auto_restore = st.toggle(
    "Enable Automatic File Recovery",
    value=True
)

if auto_restore:
    st.success(
        "Automatic recovery enabled."
    )
else:
    st.warning(
        "Automatic recovery disabled."
    )

st.divider()

# -------------------------
# Monitoring Settings
# -------------------------

st.subheader("🛰 Monitoring Settings")

monitoring = st.toggle(
    "Enable Monitoring",
    value=True
)

if monitoring:
    st.success(
        "Monitoring enabled."
    )
else:
    st.warning(
        "Monitoring disabled."
    )

st.divider()

# -------------------------
# Alerts
# -------------------------

st.subheader("🚨 Alert Management")

alert_file = "data/metadata/alert.txt"

if st.button("Clear Alerts"):

    if os.path.exists(alert_file):

        with open(alert_file, "w") as f:
            f.write("")

        st.success(
            "Alerts cleared successfully."
        )

    else:

        st.info(
            "No alerts found."
        )

st.divider()

# -------------------------
# Logs
# -------------------------

st.subheader("📜 Log Management")

log_file = "data/logs/security.log"

if st.button("Clear Logs"):

    if os.path.exists(log_file):

        open(log_file, "w").close()

        st.success(
            "Logs cleared successfully."
        )

    else:

        st.info(
            "No log file found."
        )

st.divider()

# -------------------------
# System Information
# -------------------------

st.subheader("ℹ System Information")

st.info(
    """
    File Protection System

    Features:
    • SHA-256 Integrity Verification
    • Read-Only Protection
    • Real-Time Monitoring
    • Automatic Backup Recovery
    • Security Alerts
    • Event Logging
    """
)