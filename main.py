import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup - Naeem Bhai, quotes aur key bilkul set hain
genai.configure(api_key="AIzaSyCXuHeqcOxTO43gPV9_eSjuf_5ta7uoBZ8")

# 404 Fix: Stable version ka rasta
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, system ko stable mode par reset kar diya hai.")

option = st.radio("Photo kahan se leni hai?", ("Camera", "Gallery"))

source = None
if option == "Camera":
    source = st.camera_input("Paude ki photo khainchein")
else:
    source = st.file_uploader("Gallery se select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Scan ki hui Photo", width=500)
    
    with st.spinner('AI Report bana raha hai...'):
        try:
            prompt = "Identify this plant and give its details in Urdu and English: Name, Origin, Health, and Care."
            response = model.generate_content([prompt, img])
            
            st.success("Tashkees Mukammal!")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"System Message: {e}")

st.divider()
st.info("Developed for Imran Qadri | djz")
