import boto3
import json
import streamlit as st

# --- ADDED: Import UI Lead's styles ---
from styles import apply_custom_ui, display_sidebar, render_verdict

# 1. Establish the Secure Bridge to AWS
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1', # Make sure this matches your AWS region
   
)

def analyze_scam_text(user_input):
    # 1. THE REAL BRAIN: Attempting to call AWS Bedrock (Amazon Titan Text Express)
    model_id = "amazon.titan-text-express-v1"
    
    prompt = f"You are Saterix, a security AI. Analyze this message for social engineering scams. If it's a scam, output DANGEROUS and explain why in English and Hindi. Message: {user_input}"
    
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "maxTokenCount": 512,
            "temperature": 0.1,  # Low temperature for precise, factual analysis
            "topP": 0.9
        }
    })

    try:
        response = bedrock_client.invoke_model(
            modelId=model_id,
            body=body,
            accept="application/json",
            contentType="application/json"
        )
        response_body = json.loads(response.get('body').read())
        
        # Titan's response structure is different from Claude's
        return response_body.get('results')[0].get('outputText').strip()

    except Exception as e:
        # 2. THE SAFETY NET: If AWS drops, fall back to Mock Mode
        st.info(f"Cloud Bridge Pending/Failed ({e}): Using Local Cognitive Firewall...")
        
        # --- Load Researcher's Database ---
        try:
            with open("scam_db_80.json", "r", encoding="utf-8") as f:
                db = json.load(f)
        except Exception:
            return "🛡️ **SATERIX VERDICT: ERROR**\nCould not load scam_db_80.json."

        user_input_lower = user_input.lower()
        
        # Map triggers to the categories in the JSON
        category_triggers = {
            "Digital Arrest": ["arrest", "cyber cell", "legal notice", "गिरफ्तारी", "साइबर", "সাইবার"],
            "Electricity": ["electricity", "disconnected", "unpaid bill", "बिजली", "বিদ্যুৎ"],
            "KYC/Bank": ["kyc", "bank account", "restricted", "केवाईसी", "অ্যাকাউন্ট"],
            "Government Subsidy": ["subsidy", "government", "funds", "सब्सिडी", "ভর্তুকি"]
        }

        for category, keywords in category_triggers.items():
            found = [word for word in keywords if word in user_input_lower]
            if found:
                reason = "Social engineering tactics detected."
                for scam in db.get("scams", []):
                    if scam["category"] == category:
                        reason = scam["technical_reason"]
                        break
                return f"DANGEROUS\nReason: High-pressure keywords ({', '.join(found)}) detected locally. Analysis: {reason}"
        
        return "SAFE\nNo immediate patterns detected."
    
# 2. The Streamlit Frontend Interface
st.set_page_config(page_title="Saterix AI", page_icon="🛡️")

# --- ADDED: Apply UI Lead's styles ---
apply_custom_ui()
display_sidebar()

st.title("🛡️ Saterix AI - Threat Analysis")
st.write("Upload suspicious text or SMS messages to check for scams.")

user_text = st.text_area("Paste suspicious message here:")

if st.button("Scan for Threats"):
    if user_text:
        with st.spinner("Analyzing via AWS Bedrock (Claude 3.5 Sonnet)..."):
            verdict = analyze_scam_text(user_text)
            st.success("Analysis Complete!")
            # --- MODIFIED: Use the custom UI render instead of st.write ---
            render_verdict(verdict)
    else:
        st.warning("Please enter some text to analyze.")
