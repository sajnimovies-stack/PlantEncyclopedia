import streamlit as st

st.set_page_config(page_title="Plant Identifier", layout="centered")

st.title("🌿 Plants Encyclopedia")
st.write("Welcome Naeem Bhai! Aapka Plant Identifier ab live hai.")

# Camera Input
picture = st.camera_input("Take a picture of a plant")

if picture:
    st.image(picture, caption="Aapki tasveer")
    st.success("Tasveer mil gayi! Processing shuru hai...")

# Gallery Upload
uploaded_file = st.file_uploader("Ya gallery se photo select karein", type=['jpg', 'png', 'jpeg'])
if uploaded_file:
    st.image(uploaded_file)
import streamlit as st
import google.generativeai as genai
from PIL import Image

# AI Setup
genai.configure(api_key="AIzaSyD8-bDJTcVoN-VYmFBpEH-LMQuAd2YREjU")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Plant Identifier AI", layout="centered")

st.title("🌿 Plants Encyclopedia (AI)")
st.write("Welcome Naeem Bhai! Kisi bhi paude ki photo upload karein, AI aapko uski detail batayega.")

# Selection method
option = st.radio("Photo kaise dena chahte hain?", ("Camera se khainchein", "Gallery se select karein"))

if option == "Camera se khainchein":
    source = st.camera_input("Take a picture")
else:
    source = st.file_uploader("Gallery se photo select karein", type=['jpg', 'png', 'jpeg'])

if source:
    img = Image.open(source)
    st.image(img, caption="Aapki Tasveer", use_column_width=True)
    
    with st.spinner('AI paude ko pehchan raha hai...'):
        try:
            # AI ko instruction dena
            prompt = "Identify this plant. Provide its name, scientific name, health benefits, and care instructions in Urdu and English."
            response = model.generate_content([prompt, img])
            
            st.success("Tashkees Mukammal!")
            st.markdown("### 📋 Maloomat (Information):")
            st.write(response.text)
        except Exception as e:
            st.error(f"Maaf kijiyega, AI connect nahi ho saka: {e}")

st.divider()
st.caption("Powered by Ruhaniya Suiting - Naeem Shahzad")
