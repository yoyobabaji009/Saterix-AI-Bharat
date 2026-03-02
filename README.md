# 🛡️ Saterix AI: The Cognitive Firewall for Bharat
**Track:** [Student Track] AI for Communities, Access & Public Impact  
**Team:** Loop Lords | **Live Prototype:** [https://saterix-ai-bharat-6rybjtfn4gwfjmmwgqlg7j.streamlit.app/](https://saterix-ai-bharat-6rybjtfn4gwfjmmwgqlg7j.streamlit.app/)

Saterix is a serverless, multi-lingual AI security agent engineered to protect rural Indian communities from social engineering and digital fraud. By focusing on **Contextual Intent Analysis**, Saterix bridges the digital literacy gap to secure the next billion users.

---

## 🚀 Why AI is Required?
Traditional security tools rely on static blacklists, which fail against sophisticated, fear-based social engineering. Saterix utilizes Generative AI because:
* **Intent Analysis:** It identifies psychological manipulation in "Digital Arrest" and fake electricity bill scams that keywords alone miss.
* **Vernacular Nuance:** It processes and explains threats in Hindi and Bengali that standard English-centric filters cannot parse.
* **Contextual Reasoning:** The AI layer adds value by distinguishing between legitimate utility notifications and phishing attempts through deep linguistic analysis.

---

## ⚙️ Technical Architecture (AWS-Native Patterns)
Saterix follows a resilient, serverless architecture to fulfill the "AI for Bharat" technical criteria:

```mermaid
graph TD
    User((User)) -->|Vernacular Text| Streamlit[Streamlit UI - Edge Node]
    Streamlit -->|Boto3 SDK| Bedrock[Amazon Bedrock - Titan Text Express]
    Streamlit -.->|Failover| Lambda[AWS Lambda - Security Engine]
    Lambda <-->|Secure Read| S3[(Amazon S3 - Threat Vault)]



---

## 🛡️ Graceful Degradation (Resiliency)
Engineered for rural India’s unstable connectivity, Saterix features a unique **Dual-Layer Defense**:
1. **Primary Cloud Node:** Deep analysis via Amazon Bedrock.
2. **Serverless Fallback:** If the primary connection is restricted, the **AWS Lambda** engine automatically falls back to an offline 80-point vernacular threat matrix to ensure user protection.

---

## 📂 Repository Structure
* `app.py`: Core application and multi-tier AWS integration logic (`Bedrock` -> `Lambda` -> `S3`).
* `scam_db_80.json`: 80-point multi-lingual behavioral threat database.
* `styles.py`: Custom security-focused CSS and UI/UX components.
* `requirements.txt`: Python dependency manifest (including `boto3` for AWS connectivity).

---

## 🛣️ Roadmap
* **Phase 2:** Integration of **Amazon Transcribe** to analyze WhatsApp voice notes for social engineering signatures.
* **Phase 3:** Deployment of a WhatsApp bot interface via **Amazon API Gateway**.

---
Built by **Puskar Das** & **Team Loop Lords** for the AI for Bharat Student Track.
