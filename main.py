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
