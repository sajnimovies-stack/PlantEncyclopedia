import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup - Naeem Bhai yahan aapki nayi key hai
genai.configure(api_key="AIzaSyAQeqVe_1bJpHToQYOAu8zwl3948Ztor_U")

# 404 Fix: Model ko direct version ke sath call karna
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    generation_config={"target_output_uri": "v1beta"}
)

st.set_page_config(page_title="Plant Expert AI", layout="wide")

st.title("🌿 Plants Encyclopedia & Doctor AI")
st.write("Welcome Naeem Bhai! Mobile se photo khainchein.")

option = st.radio("Zariya select karein:", ("Camera", "Gallery"))

source = None
if option == "Camera":
    source = st.camera_input("Paude ki photo khainchein")
else:
    source = st.file_uploader("Photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Photo", width=400)
    
    with st.spinner('AI Report tayyar kar raha hai...'):
        try:
            prompt = "Identify this plant and its health status in Urdu and English."
            # Direct generation
            response = model.generate_content([prompt, img])
            
            st.success("Report Taiyar Hai!")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Naya Error: {e}")

st.divider()
st.info("Developed for Imran Qadri | djz")
