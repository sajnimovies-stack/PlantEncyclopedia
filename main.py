import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

# Model ka naam bina 'models/' ke check karte hain, agar 404 aaye toh 'models/gemini-1.5-flash' kar dein
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Welcome Naeem Bhai! Mobile camera se full screen photo khainchein.")

option = st.radio("Option select karein:", ("Camera (Full Screen)", "Gallery se upload karein"))

source = None
if option == "Camera (Full Screen)":
    source = st.camera_input("Paude ki saaf tasveer khainchein")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Scan ki hui Photo", use_container_width=True)
    
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
            response = model.generate_content([prompt, img])
            st.success("Tashkees Mukammal!")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

# Aapki matlooba tabdeeli yahan hai:
st.divider()
st.info("Developed for Imran Qadri | djz")
