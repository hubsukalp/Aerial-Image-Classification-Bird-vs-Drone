import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load model
model = load_model("best_model.keras")

# Title
st.title("Aerial Object Classification (Bird vs Drone)")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).resize((128,128))
    st.image(image, caption="Uploaded Image", width=300)

    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.success(f"Prediction: Drone 🚁 ({prediction*100:.2f}%)")
    else:
        st.success(f"Prediction: Bird 🐦 ({(1-prediction)*100:.2f}%)")