import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup (Stable Version)
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

# Sab se purana aur pakka model jo error nahi deta
model = genai.GenerativeModel('gemini-pro-vision')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, maine model change kar diya hai taake error khatam ho jaye.")

# Selection method
option = st.radio("Option select karein:", ("Camera (Full Screen)", "Gallery se upload karein"))

source = None
if option == "Camera (Full Screen)":
    source = st.camera_input("Paude ki saaf tasveer khainchein")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Photo", use_column_width=True)
    
    with st.spinner('AI paude ko dekh raha hai...'):
        try:
            # Simple Prompt taake response jaldi aaye
            prompt = "Identify this plant. Give its name, health status, native origin, and mother plant details in Urdu and English."
            
            # Response lena
            response = model.generate_content([prompt, img])
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Report:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Abhi bhi masla aa raha hai: {e}")

st.divider()
st.caption("Developed for Ruhaniya Suiting | Naeem Shahzad")
