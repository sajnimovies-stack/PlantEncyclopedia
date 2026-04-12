import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Expert AI", layout="wide") # Layout wide rakha hai

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Naeem Bhai, ab aap full screen camera istemal kar sakte hain aur paude ki beemariyon ka bhi pata laga sakte hain.")

# Selection method
option = st.radio("Option select karein:", ("Camera (Full Screen)", "Gallery se upload karein"))

source = None

if option == "Camera (Full Screen)":
    # Camera input ko container mein rakha hai taake bara nazar aaye
    source = st.camera_input("Paude ki saaf tasveer khainchein")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Scan ki hui Photo", use_column_width=True)
    
    with st.spinner('AI gehri tashkees (Deep Analysis) kar raha hai...'):
        try:
            # Mazeed tafseel mangne ke liye prompt ko bara kiya hai
            prompt = """
            Identify this plant and provide a detailed report in Urdu and English:
            1. Name and Scientific Name.
            2. Native Origin: Ye pauda asal mein kis jagah ya mulk se belong karta hai?
            3. Mother Plant: Iska mother plant kaisa hota hai aur ye kaise barhta hai?
            4. Health Status & Diseases: Is paude ko kaunsi beemariyan lag sakti hain ya abhi is photo mein koi beemari nazar aa rahi hai?
            5. Care Instructions: Pani aur dhoop ki zaroorat.
            """
            
            response = model.generate_content([prompt, img])
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Paude ki Mukammal Report:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"System busy hai ya koi masla aa gaya hai: {e}")

st.divider()
st.caption("Developed for Ruhaniya Suiting | Naeem Shahzad")
