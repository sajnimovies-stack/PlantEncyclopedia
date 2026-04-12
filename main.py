import streamlit as st
from google import genai
from PIL import Image

# Latest AI Setup (Nayi Library)
# Naeem Bhai, ye naya tareeqa hai jo error nahi deta
client = genai.Client(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Welcome Naeem Bhai! Mobile camera se photo khainchein.")

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
            # Report ka sawal (Prompt)
            prompt = """
            Identify this plant and provide a detailed report in Urdu and English:
            1. Name and Scientific Name.
            2. Native Origin (Asal jagah).
            3. Mother Plant details.
            4. Health Status & Diseases (Beemariyan).
            5. Care Instructions.
            """
            
            # Naye system mein model call karne ka sahi tareeqa
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=[prompt, img]
            )
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Report:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")

# Aapki branding yahan update kar di hai
st.divider()
st.info("Developed for Imran Qadri | djz")
