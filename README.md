🛡️ Saterix AI: The Cognitive Firewall for Bharat
Track: [Student Track] AI for Communities, Access & Public Impact

Team: Loop Lords | Live Prototype: https://saterix-ai-bharat-6rybjtfn4gwfjmmwgqlg7j.streamlit.app/

Saterix is a serverless, multi-lingual AI security agent engineered to protect rural Indian communities from social engineering and digital fraud. By focusing on Contextual Intent Analysis, Saterix bridges the digital literacy gap to secure the next billion users.

🚀 Why AI is Required?
Traditional security tools rely on static blacklists, which fail against sophisticated, fear-based social engineering. Saterix utilizes Generative AI because:

Intent Analysis: It identifies psychological manipulation in "Digital Arrest" and fake electricity bill scams that keywords alone miss.

Vernacular Nuance: It processes and explains threats in Hindi and Bengali that standard English-centric filters cannot parse.

Contextual Reasoning: The AI layer adds value by distinguishing between legitimate utility notifications and phishing attempts through deep linguistic analysis.

⚙️ Technical Architecture (AWS-Native Patterns)
Saterix follows a resilient, serverless architecture to maximize scalability and fulfill the "AI for Bharat" technical criteria:

Brain (Amazon Bedrock): Utilizes Amazon Titan Text Express for zero-shot vernacular intent parsing and threat categorization.

Compute (AWS Lambda): Orchestrates backend logic via serverless execution, ensuring the system scales instantly for millions of users.

Storage (Amazon S3): Hosts the Saterix Threat Vault, a centralized repository for our 80-point multi-lingual threat matrix and future audio payloads.

Security (AWS SDK): Built with boto3 to manage secure, encrypted communication between the edge frontend and the AWS cloud backbone.

🛡️ Graceful Degradation (Resiliency)
Engineered for rural India’s unstable connectivity, Saterix features a unique Dual-Layer Defense. If the primary AWS Bedrock connection is restricted or unreachable, the AWS Lambda engine automatically falls back to an offline 80-point vernacular threat matrix to ensure the user is never unprotected.

📂 Repository Structure
app.py: Core application and multi-tier AWS integration logic (Bedrock -> Lambda -> S3).

scam_db_80.json: 80-point multi-lingual behavioral threat database.

styles.py: Custom security-focused CSS and UI/UX components.

requirements.txt: Python dependency manifest (including boto3 for AWS connectivity).

🛣️ Roadmap
Phase 2: Integration of Amazon Transcribe/Whisper to analyze WhatsApp voice notes for social engineering signatures.

Phase 3: Deployment of a WhatsApp bot interface via Amazon API Gateway.
