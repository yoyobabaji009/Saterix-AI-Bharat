# 🛡️ Saterix AI: The Cognitive Firewall for Bharat
**Track:** [Student Track] AI for Communities, Access & Public Impact  
**Team:** Loop Lords | **Live Prototype:** [https://saterix-ai-bharat-6rybjtfn4gwfjmmwgqlg7j.streamlit.app/](https://saterix-ai-bharat-6rybjtfn4gwfjmmwgqlg7j.streamlit.app/)

Saterix is a serverless, multimodal AI security agent engineered to protect rural Indian communities from digital fraud. By focusing on **Contextual Intent Analysis**, Saterix bridges the digital literacy gap to secure the next billion users.

---

## 🚀 Why AI is Required?
Traditional security tools rely on static blacklists, which fail against sophisticated, fear-based social engineering. Saterix utilizes Generative AI to:
* **Analyze Intent:** Identify psychological manipulation in "Digital Arrest" and fake electricity bill scams.
* **Handle Vernacular Nuance:** Process and explain threats in Hindi, Bengali, and Tamil that standard English-centric filters miss.
* **Contextual Reasoning:** Distinguish between a legitimate utility notification and a phishing attempt through linguistic analysis.

---

## ⚙️ Technical Architecture (AWS-Native Patterns)
Saterix follows a resilient, serverless architecture to maximize scalability and minimize latency:

* **AI Engine:** **Amazon Bedrock** (Amazon Titan Text Express & Claude 3.5 Sonnet) for deep intent analysis and vernacular translation.
* **Compute:** **AWS Lambda** for serverless back-end orchestration and API handling.
* **Storage:** **Amazon S3** for secure, temporary buffering of uploaded screenshots and audio evidence.
* **Development:** Built using **Kiro** for spec-driven development and **Amazon Q** for code optimization.



---

## 🛡️ Graceful Degradation (Resiliency)
Engineered for rural India’s unstable connectivity, Saterix features a unique **Local Cognitive Firewall**. If the AWS cloud connection is restricted or unreachable, the system automatically falls back to an offline 80-point vernacular threat matrix to ensure the user is never left unprotected.

---

## 📂 Repository Structure
* `app.py`: Core Streamlit application and AWS integration logic.
* `styles.py`: Custom security-focused CSS and UI/UX components.
* `scam_db_80.json`: 80-point multi-lingual local threat database.
* `requirements.md`: Comprehensive functional and non-functional specifications.
* `design.md`: Detailed system architecture and data flow diagrams.
