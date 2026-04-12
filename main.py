import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup
# Naeem bhai, ye API key aur model ka rasta ab bilkul sahi hai
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")
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
    # Naye Streamlit update ke mutabik 'width' ko set kiya hai
    st.image(img, caption="Aapki Scan ki hui Photo", width=700)
    
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

# Aapki branding yahan hai
st.divider()
st.info("Developed for Imran Qadri | djz")
