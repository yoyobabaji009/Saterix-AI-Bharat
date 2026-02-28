import streamlit as st

def apply_custom_ui():
    # 1. CSS Injection: Design the "Security Dashboard" Look
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main {
            background-color: #0e1117;
            color: #ffffff;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            color: #ffffff;
        }

        .threat-box {
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #ff4b4b;
            background-color: #1a1c24;
            margin-top: 10px;
        }

        .threat-box::before {
            content: "⚠️ THREAT DETECTED";
            display: block;
            font-weight: 700;
            font-size: 1.1rem;
            color: #ff4b4b;
            margin-bottom: 10px;
        }

        .safe-box {
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #28a745;
            background-color: #1a1c24;
            margin-top: 10px;
        }

        .safe-box::before {
            content: "✅ SAFE";
            display: block;
            font-weight: 700;
            font-size: 1.1rem;
            color: #28a745;
            margin-bottom: 10px;
        }

        .sidebar-status {
            color: #f1c40f;
            font-weight: bold;
        }

        /* Make Scan button large and mobile-friendly */
        div.stButton > button {
            width: 100%;
            padding: 16px;
            font-size: 1.1rem;
            font-weight: 700;
            background-color: #ff4b4b;
            color: #ffffff;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        div.stButton > button:hover {
            background-color: #e03c3c;
        }
        </style>
        """, unsafe_allow_html=True)


def display_sidebar():
    with st.sidebar:
        st.title("🛡️ Saterix AI")
        st.markdown('<p class="sidebar-status">🟡 System Status: Local Prototype Mode</p>', unsafe_allow_html=True)
        st.info("**About Saterix**\n\nSaterix is a cognitive firewall for rural users, designed to detect social engineering scams and protect communities across Bharat.")


def render_verdict(verdict_text):
    if "DANGEROUS" in verdict_text or "DANGER" in verdict_text:
        st.markdown(
            f'<div class="threat-box">{verdict_text}</div>',
            unsafe_allow_html=True
        )
    elif "SAFE" in verdict_text:
        st.markdown(
            f'<div class="safe-box">{verdict_text}</div>',
            unsafe_allow_html=True
        )
    else:
        st.write(verdict_text)
