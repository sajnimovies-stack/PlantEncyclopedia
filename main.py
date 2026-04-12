import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup - Nayi API Key jo aapne di thi
genai.configure(api_key="AIzaSyAQeqVe_1bJpHToQYOAu8zwl3948Ztor_U")

# Sab se stable model config
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, ab check karein. System bilkul reset kar diya hai.")

option = st.radio("Photo kahan se leni hai?", ("Camera", "Gallery"))

source = None
if option == "Camera":
    source = st.camera_input("Paude ki saaf photo khainchein")
else:
    source = st.file_uploader("Gallery se select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Scan ki hui Photo", width=500)
    
    with st.spinner('AI Report bana raha hai...'):
        try:
            # Simple aur Seedha Prompt
            prompt = """
            Identify this plant and give a report in Urdu and English:
            1. Name
            2. Native Origin
            3. Health/Diseases
            4. Care Tips
            """
            
            # Seedha call bina kisi faltu config ke
            response = model.generate_content([prompt, img])
            
            if response.text:
                st.success("Tashkees Mukammal!")
                st.write(response.text)
            else:
                st.warning("AI ne response nahi diya, dobara photo khainchein.")
                
        except Exception as e:
            # Agar koi error aaye toh wo yahan dikhega
            st.error(f"System Message: {e}")

st.divider()
st.info("Developed for Imran Qadri | djz")
