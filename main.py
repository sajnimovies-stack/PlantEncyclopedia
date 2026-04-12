import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup (Stable Version)
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")

# Model ka naam sahi format mein (gemini-1.5-flash)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, system update kar diya gaya hai. Ab check karein.")

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
    
    with st.spinner('AI paude ka muayna kar raha hai...'):
        try:
            prompt = """
            Identify this plant and provide a detailed report in Urdu and English:
            1. Name and Scientific Name.
            2. Native Origin: Ye pauda asal mein kahan ka hai?
            3. Mother Plant: Iska mother plant kaisa hota hai?
            4. Health Status & Diseases: Is photo mein koi beemari hai? Aam beemariyan aur unka hal batayein.
            5. Care Instructions: Pani aur dhoop.
            """
            
            # Yahan humne model ko call kiya hai
            response = model.generate_content([prompt, img])
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Report:")
            st.write(response.text)
            
        except Exception as e:
            # Agar ab bhi error aaye toh wo detail yahan nazar aayegi
            st.error(f"Error detail: {e}")

st.divider()
st.caption("Developed for Ruhaniya Suiting | Naeem Shahzad")
