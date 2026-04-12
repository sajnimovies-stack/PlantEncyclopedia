import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup - Nayi API Key
genai.configure(AIzaSyCXuHeqcOxTO43gPV9_eSjuf_5ta7uoBZ8")

# --- 404 FIX: Yahan model ka naam tabdil kiya hai ---
# Hum 'gemini-1.5-flash-latest' use karenge jo 404 nahi deta
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, system ko bypass mode par set kar diya hai.")

option = st.radio("Photo Source:", ("Camera", "Gallery"))

source = None
if option == "Camera":
    source = st.camera_input("Paude ki photo khainchein")
else:
    source = st.file_uploader("Gallery se select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Photo", width=500)
    
    with st.spinner('AI Process kar raha hai...'):
        try:
            prompt = "Identify this plant and describe its health in Urdu and English."
            
            # Simple Call
            response = model.generate_content([prompt, img])
            
            st.success("Report Taiyar!")
            st.write(response.text)
            
        except Exception as e:
            # Agar ab bhi error aaye toh hum model badal kar check karenge
            st.error(f"Try alternative: {e}")
            st.info("Naeem bhai, agar error 404 hai toh aapko Google AI Studio se 'Nayi API Key' banani hogi.")

st.divider()
st.info("Developed for Imran Qadri | djz")
