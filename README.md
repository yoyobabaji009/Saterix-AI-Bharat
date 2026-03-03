# 🛡️ Saterix AI: Cognitive Firewall for Rural Bharat

**Team Loop Lords | AI for Bharat Competition 2026**

![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Security Hardened](https://img.shields.io/badge/Security-L3_Hardened-red?style=for-the-badge&logo=shield)
![Latency](https://img.shields.io/badge/Latency-~280ms-green?style=for-the-badge&logo=lightning)
![AI Model](https://img.shields.io/badge/Model-Llama_3.3_70B-blue?style=for-the-badge&logo=meta)

Saterix is a multi-layered security engine designed to protect vernacular users from social engineering scams (WBSEDCL utility fraud, banking phishing, and KYC scams). By leveraging ultra-fast LPU inference and behavioral analysis, Saterix intercepts threats in real-time before users can be manipulated.

---

## ⚙️ The Saterix Defense-in-Depth

Saterix runs every message through a 3-layer security tunnel to ensure maximum protection for rural users:

1. **LAYER 1: LOCAL HEURISTICS (REGEX)**
   - Instant scan for suspicious URL shorteners (bit.ly, t.me, wa.me).
   - Blocks impersonated utility domains (e.g., `wbsedcl-bill-pay.com`).

2. **LAYER 2: INSTRUCTION ISOLATION (XML TAGGING)**
   - Uses `<UNTRUSTED_DATA>` encapsulation to isolate user input from the AI's core logic.
   - Prevents "Prompt Injection" attacks aimed at hijacking the AI's instructions.

3. **LAYER 3: COGNITIVE INTENT ANALYSIS (GROQ LPU)**
   - Powered by **Llama 3.3 (70B)** with sub-300ms latency.
   - Analyzes "Psychological Triggers" in **Bengali, Hindi, and Hinglish**.

---

## 🚀 Key Features

* **⚡ LPU-Powered Inference:** Achieves **~280ms response latency** via **Groq LPU™**, ensuring the user is warned instantly.
* **🎙️ Bimodal Accessibility:** Native **Speech-to-Text (STT)** integration, enabling voice-based scanning for users with low digital literacy.
* **🇮🇳 Vernacular Intelligence:** Optimized for local social engineering patterns common in West Bengal.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit |
| **LLM Engine** | Llama 3.3 70B (**Groq LPU**) |
| **Database** | Amazon DynamoDB (Threat Matrix) |
| **Voice Engine** | Streamlit Mic Recorder (STT) |
| **Security Layer** | XML Delimiter Hardening |

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/yoyobabaji009/Saterix-AI-Bharat](https://github.com/yoyobabaji009/Saterix-AI-Bharat)
cd Saterix-AI-Bharat

2. Install dependencies
pip install -r requirements.txt

3. Configure Secrets:
Create a folder named .streamlit and a file inside it called secrets.toml:

GROQ_API_KEY = "your_groq_key_here"
AWS_ACCESS_KEY_ID = "your_aws_key_here"
AWS_SECRET_ACCESS_KEY = "your_aws_secret_here"

4. Run Saterix
streamlit run app.py


Developed by Puskar Das & Team Loop Lords

Final GitHub Push
To apply this fixed version to your repository, run these commands in your terminal:
```bash
git add README.md
git commit -m "🔧 Fix: Resolved Mermaid rendering error and optimized document layout"
git push origin main
