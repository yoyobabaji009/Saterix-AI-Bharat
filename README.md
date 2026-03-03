# 🛡️ Saterix AI: Cognitive Firewall for Rural Bharat

**Team Loop Lords | AI for Bharat Competition 2026**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://saterix-ai-bharat.streamlit.app/)
![Security Hardened](https://img.shields.io/badge/Security-L3_Hardened-red?style=for-the-badge&logo=shield)
![Latency](https://img.shields.io/badge/Latency-~280ms-green?style=for-the-badge&logo=lightning)
![AI Model](https://img.shields.io/badge/Model-Llama_3.3_70B-blue?style=for-the-badge&logo=meta)

Saterix is a multi-layered security engine designed to protect vernacular users from social engineering scams (WBSEDCL utility fraud, banking phishing, and KYC scams). By leveraging ultra-fast LPU inference and behavioral analysis, Saterix intercepts threats in real-time before users can be manipulated.

---

## ⚙️ System Workflow

The architecture follows a "Defense-in-Depth" approach. Simple threats (malicious links) are caught by local heuristics, while complex social engineering is analyzed by the Llama 3.3 engine.

```mermaid
graph TD
    A[User Input: SMS/Voice] --> B{Layer 1: Heuristics}
    B -- Suspicious Link --> C[🚨 FLAG: DANGEROUS]
    B -- Clear --> D[Layer 2: Hardened Context]
    D --> E[XML Isolation: UNTRUSTED_DATA]
    E --> F[Groq LPU: Llama 3.3 70B]
    F --> G{Intent Analysis}
    G -- Malicious Pattern --> C
    G -- Safe Pattern --> H[✅ FLAG: SAFE]
    
    style C fill:#FF4B4B,stroke:#333,stroke-width:2px,color:#fff
    style H fill:#28a745,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#f96,stroke:#333,stroke-width:4px


🚀 Key Features:-
LPU-Powered Inference: Achieves ~280ms response latency using Llama 3.3 (70B) via Groq LPU™, allowing for instant threat detection.
Hardened Security: Implements XML-tag isolation and system-prompt hardening to neutralize "Prompt Injection" and instruction-overriding attacks.
Bimodal Accessibility: Integrated Speech-to-Text (STT) support, allowing rural users to scan messages via voice—bridging the digital literacy gap.
Vernacular Intelligence: Specifically tuned for Bengali, Hindi, and Hinglish social engineering patterns common in West Bengal.

🏗️ Technical Architecture:-
Saterix is built on a modular stack designed for scalability and sub-second response times:
L1: Heuristic Engine: Instant regex-based scanning for dangerous URL shorteners (bit.ly, t.me) and impersonated utility domains.
L2: Instruction Layering: Encapsulates user input within <UNTRUSTED_DATA> delimiters, ensuring the LLM treats input as data, not commands.
L3: Cognitive Intent Engine: Deep semantic analysis via Groq to detect psychological triggers like artificial urgency, threat of service disconnection, and unofficial contact channels.
Backend: Python-based Streamlit application hosted with integrated AWS DynamoDB connectivity for the Vernacular Threat Matrix.

🛠️ Tech Stack:-
Frontend: Streamlit
LLM Engine: Llama 3.3 70B (Groq LPU)
Database: Amazon DynamoDB (Vernacular Threat Matrix)
Voice Engine: Streamlit Mic Recorder (Speech-to-Text)
Security Layer: XML Delimiter Hardening

🚀 Installation & Usage:-

Clone the repository:

Bash
git clone [https://github.com/yoyobabaji009/Saterix-AI-Bharat](https://github.com/yoyobabaji009/Saterix-AI-Bharat)

Install dependencies:
Bash
pip install -r requirements.txt

Configure Secrets:
Create .streamlit/secrets.toml and add your GROQ_API_KEY and AWS_CREDENTIALS.

Run Saterix:
Bash
streamlit run app.py