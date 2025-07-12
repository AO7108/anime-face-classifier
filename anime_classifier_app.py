import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(page_title="Anime Face Classifier")
st.title("🎌 Anime Character Classifier")

# Load the trained model
model = tf.keras.models.load_model("models/anime_cnn_model_v2.h5")

# Replace with your actual class names
class_names = ["Emilia", "Gojo", "Hua Cheng", "Luffy", "Okabe"]

uploaded_file = st.file_uploader("Upload an anime image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # === IMPORTANT === Resize to match model's input shape exactly!
    image = image.resize((128, 128))

    # Convert to numpy and normalize
    img_array = np.array(image).astype("float32") / 255.0

    # Add batch dimension (1, 128, 128, 3)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Output
    st.success(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}%")

    st.subheader("Breakdown:")
    for i, prob in enumerate(prediction[0]):
        st.write(f"{class_names[i]}: {prob * 100:.2f}%")