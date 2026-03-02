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
    Lambda <--- |Secure Read| S3[(Amazon S3 - Threat Vault)]
