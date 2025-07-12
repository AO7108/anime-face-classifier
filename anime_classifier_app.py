import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import os

# ---------------------------
# ✅ Page Config
# ---------------------------
st.set_page_config(page_title="Anime Face Classifier")
st.title("🎌 Anime Character Classifier")

# ---------------------------
# ✅ Constants
# ---------------------------
MODEL_PATH = "models/anime_cnn_model_v2.h5"
MODEL_URL = "https://drive.google.com/uc?id=1DWlAbW9-XLafX1AB6QJhmrnjRGDjM12u"
CLASS_NAMES = ["Emilia", "Gojo", "Hua Cheng", "Luffy", "Okabe"]

# ---------------------------
# ✅ Download model if missing
# ---------------------------
if not os.path.exists(MODEL_PATH):
    st.info("🔄 Model not found locally. Downloading from Google Drive...")
    try:
        import gdown
    except ImportError:
        st.error("gdown is not installed. Please add gdown to requirements.txt.")
        st.stop()

    os.makedirs("models", exist_ok=True)
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

# ---------------------------
# ✅ Load Model
# ---------------------------
model = tf.keras.models.load_model(MODEL_PATH)

# ---------------------------
# ✅ File Uploader
# ---------------------------
uploaded_file = st.file_uploader("📸 Upload an anime face image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess image
    image = image.resize((128, 128))
    img_array = np.array(image).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Shape: (1, 128, 128, 3)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Output
    st.success(f"Prediction: {predicted_class}")
    st.write(f"🧠 Confidence: {confidence:.2f}%")

    st.subheader("📊 Class Breakdown:")
    for i, prob in enumerate(prediction[0]):
        st.write(f"- {CLASS_NAMES[i]}: {prob * 100:.2f}%")