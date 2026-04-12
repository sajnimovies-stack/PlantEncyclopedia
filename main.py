import streamlit as st
from google import genai
from PIL import Image

# AI Setup (Naya Package 2026)
client = genai.Client(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Welcome Naeem Bhai! Mobile camera se full screen photo khainchein.")

# Selection method
option = st.radio("Option select karein:", ("Camera (Full Screen)", "Gallery se upload karein"))

source = None
if option == "Camera (Full Screen)":
    source = st.camera_input("Paude ki saaf tasveer khainchein")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    # Image display setting
    st.image(img, caption="Aapki Scan ki hui Photo", width=700)
    
    with st.spinner('AI gehri tashkees (Deep Analysis) kar raha hai...'):
        try:
            prompt = """
            Identify this plant and provide a detailed report in Urdu and English:
            1. Name and Scientific Name.
            2. Native Origin: Ye pauda asal mein kis jagah se belong karta hai?
            3. Mother Plant: Iska mother plant kaisa hota hai?
            4. Health Status & Diseases: Is photo mein koi beemari nazar aa rahi hai?
            5. Care Instructions: Pani aur dhoop ki zaroorat.
            """
            
            # Naya Model Call tareeqa
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=[prompt, img]
            )
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Paude ki Mukammal Report:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"System busy hai ya koi masla aa gaya hai: {e}")

# Aapki final branding
st.divider()
st.info("Developed for Imran Qadri | djz")
