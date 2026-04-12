import streamlit as st
import google.generativeai as genai
from PIL import Image

# Line 6 Fix: Yahan quotes sahi kar diye hain
genai.configure(api_key="AIzaSyCXuHeqcOxTO43gPV9_eSjuf_5ta7uoBZ8")

# Stable Model
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, syntax error theek kar diya hai. Ab check karein.")

option = st.radio("Photo Source:", ("Camera", "Gallery"))

source = None
if option == "Camera":
    source = st.camera_input("Paude ki photo khainchein")
else:
    source = st.file_uploader("Gallery se select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Photo", width=500)
    
    with st.spinner('AI Report bana raha hai...'):
        try:
            prompt = "Identify this plant and describe its health in Urdu and English."
            response = model.generate_content([prompt, img])
            
            st.success("Report Taiyar!")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")

st.divider()
st.info("Developed for Imran Qadri | djz")
