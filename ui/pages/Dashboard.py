import streamlit as st
import json
import os

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Security Dashboard")

st.divider()

# -------------------------
# Status Section
# -------------------------

status_file = "data/metadata/status.json"

if os.path.exists(status_file):

    with open(status_file, "r") as f:
        status = json.load(f)

    file_name = status.get("file", "Unknown")
    monitor_status = status.get("monitoring", False)

else:

    file_name = "No File Protected"
    monitor_status = False

# -------------------------
# Stats Section
# -------------------------

stats_file = "data/metadata/stats.json"

if os.path.exists(stats_file):

    with open(stats_file, "r") as f:
        stats = json.load(f)

else:

    stats = {
        "protected": 0,
        "threats": 0,
        "restored": 0
    }

# -------------------------
# Dashboard Cards
# -------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Protected Files",
        stats["protected"]
    )

with col2:

    st.metric(
        "Threats Detected",
        stats["threats"]
    )

with col3:

    st.metric(
        "Files Restored",
        stats["restored"]
    )

st.divider()

# -------------------------
# Protected File Info
# -------------------------

st.subheader("📁 Protected File")

st.info(file_name)

# -------------------------
# Monitoring Status
# -------------------------

st.subheader("🛰 Monitoring Status")

if monitor_status:

    st.success(
        "Monitoring Active"
    )

else:

    st.warning(
        "Monitoring Not Running"
    )

# -------------------------
# Alert Section
# -------------------------

alert_file = "data/metadata/alert.txt"

if os.path.exists(alert_file):

    with open(alert_file, "r") as f:

        alert = f.read().strip()

    if alert:

        st.error(
            f"⚠ {alert}"
        )

st.divider()

# -------------------------
# Quick Status
# -------------------------

st.subheader("📌 System Overview")

st.write(
    """
    - File Integrity Protection Enabled
    - Automatic Backup Recovery Enabled
    - Real-Time Monitoring Enabled
    - Security Logging Enabled
    """
)