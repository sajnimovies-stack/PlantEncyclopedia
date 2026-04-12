import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup - Stable API Version
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

# Forcefully using a stable model path
model = genai.GenerativeModel('gemini-1.5-flash')

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
            # Simple Prompt for faster response
            prompt = "Identify this plant. Tell its name, native origin, mother plant details, and any diseases visible in Urdu and English."
            
            response = model.generate_content([prompt, img])
            
            if response.text:
                st.success("Tashkees Mukammal!")
                st.markdown("### 📋 Report:")
                st.write(response.text)
            else:
                st.warning("AI ne jawab nahi diya, dobara koshish karein.")
                
        except Exception as e:
            st.error(f"Error Detail: {e}")

st.divider()
st.info("Developed for Imran Qadri | djz")
