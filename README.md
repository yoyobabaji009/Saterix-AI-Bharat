# 🛡️ Saterix AI: The Cognitive Firewall for Bharat
**Track:** [Student Track] AI for Communities, Access & Public Impact  
**Team:** Loop Lords  
**Live Prototype:** [https://saterix-ai-firewall.streamlit.app](https://saterix-ai-firewall.streamlit.app)

Saterix is a resilient Multimodal AI Security Agent designed to protect rural and elderly Indian communities from digital fraud. By analyzing the *intent* of communications, Saterix bridges the digital literacy gap to secure the next billion users.

---

## 🚀 Why AI is Required
Traditional security tools rely on static blacklists and keyword matching, which fail against sophisticated, fear-based social engineering. Saterix requires **Generative AI** to:
* **Understand Intent:** Identify psychological manipulation in "Digital Arrest" and fake electricity bill scams.
* **Vernacular Nuance:** Process threats in Hindi and Bengali that standard filters miss.
* **Contextual Reasoning:** Distinguish between a legitimate bank notification and a phishing attempt.

---

## ⚙️ Technical Architecture (AWS-Native Patterns)
Saterix is built using a serverless architecture to ensure high availability and zero-cost scaling:

* **AI Engine:** **Amazon Bedrock** (Claude 3.5 Sonnet & Titan) for deep intent analysis and vernacular translation.
* **Compute:** **AWS Lambda** handles the serverless back-end orchestration.
* **Storage:** **Amazon S3** provides secure, temporary buffering for uploaded evidence (screenshots/audio).
* **Intelligence:** **Amazon Transcribe** converts vernacular voice notes into text for AI analysis.
* **Development:** Built using **Kiro** for spec-driven development and **Amazon Q** for code optimization.

---

## 🛡️ Graceful Degradation (Resiliency)
Engineered for rural India’s unstable connectivity, Saterix features a unique **Local Cognitive Firewall**. If the AWS cloud connection is restricted, the system automatically falls back to a local 80-point vernacular threat matrix to ensure the user is never left unprotected.

---

## 📂 Repository Structure
* `app.py`: Main Streamlit application and AWS integration logic.
* `styles.py`: Custom CSS and security-focused UI components.
* `scam_db_80.json`: 80-point multi-lingual local threat database.
* `requirements.md`: Detailed functional and non-functional specifications.
* `design.md`: System architecture and data flow diagrams.# Saterix AI: The Cognitive Firewall for Bharat 🛡️

**Track:** Student Track (AI for Communities, Access & Public Impact)
**Team:** [Loop Lords]

## 🚀 Project Overview
Saterix is a Multimodal AI Security Agent powered by **Amazon Bedrock** (Claude 3.5 Sonnet + Titan Multimodal). It acts as a digital bodyguard for rural Indians, detecting vernacular scams (Digital Arrests, Fake UPI QRs) that traditional tools miss.

## 🛠️ Tech Stack
- **AI Engine:** Amazon Bedrock (Claude 3.5 Sonnet, Titan Multimodal)
- **Voice Intelligence:** Amazon Transcribe
- **Compute:** AWS Lambda (Serverless)
- **Frontend:** Streamlit
- **Dev Tools:** Amazon Q, Kiro IDE

## 📂 Repository Structure
- `requirements.md`: User stories and functional specs.
- `design.md`: System architecture and data flow diagrams.
- `Presentation.pdf`: The official idea pitch deck.
