import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


import streamlit as st
import os

from core.start_protection import protect_file

# Page configuration
st.set_page_config(
    page_title="File Protection System",
    page_icon="🛡",
    layout="wide"
)

# Header
st.title("🛡 File Protection System")

st.subheader(
    "Real-Time File Monitoring & Auto Recovery"
)

st.write(
    """
    Protect important files from unauthorized modifications.
    
    Features:
    - SHA-256 Integrity Verification
    - Automatic Backup Creation
    - Real-Time Monitoring
    - Auto Recovery
    - Security Alerts
    """
)

st.divider()

# Upload section

st.header("📁 Upload File")

uploaded_file = st.file_uploader(
    "Choose a file"
)

if uploaded_file:

    os.makedirs(
        "protected_files",
        exist_ok=True
    )

    file_path = os.path.join(
        "protected_files",
        uploaded_file.name
    )

    # Save uploaded file
    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        f"{uploaded_file.name} uploaded successfully."
    )

    st.write(
        f"File Path: {file_path}"
    )

    if st.button(
        "🛡 Protect File"
    ):

        result = protect_file(
            file_path
        )

        if result:

            st.success(
                "Protection started successfully."
            )

        else:

            st.error(
                "Failed to start protection."
            )

st.divider()

# Feature cards

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "🔒 Read-Only Protection"
    )

with col2:
    st.info(
        "🛰 Real-Time Monitoring"
    )

with col3:
    st.info(
        "♻ Auto Recovery"
    )