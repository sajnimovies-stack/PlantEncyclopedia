import streamlit as st
from google import genai
from PIL import Image

# Naya AI Setup (2026 SDK)
# Naeem Bhai, apni purani key yahan check kar lein ya nayi laga dein
client = genai.Client(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Welcome Naeem Bhai! System updated to Latest SDK.")

option = st.radio("Option select karein:", ("Camera (Full Screen)", "Gallery se upload karein"))

source = None
if option == "Camera (Full Screen)":
    source = st.camera_input("Paude ki saaf tasveer khainchein")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Scan ki hui Photo", width=500)
    
    with st.spinner('AI analysis kar raha hai...'):
        try:
            prompt = """
            Identify this plant and provide a detailed report in Urdu and English:
            1. Name and Scientific Name.
            2. Native Origin (Asal jagah).
            3. Mother Plant details.
            4. Health Status & Diseases (Beemariyan).
            5. Care Instructions.
            """
            
            # Naye system (google-genai) ka sahi call
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=[prompt, img]
            )
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Report:")
            st.write(response.text)
            
        except Exception as e:
            # Agar 404 aaye toh yahan message dikhayega
            st.error(f"Error: {e}")

# Footer Branding
st.divider()
st.info("Developed for Imran Qadri | djz")
