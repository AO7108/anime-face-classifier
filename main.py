import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# Load the trained model
model = load_model("models/anime_cnn_model_v2.h5")  # or anime_cnn_model.h5 if using older version

def load_and_prepare_image(img_path, target_size=(128, 128)):
    """Load image and prepare it for prediction"""
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def predict(img_path):
    """Run prediction on a single image"""
    img_array = load_and_prepare_image(img_path)
    prediction = model.predict(img_array)
    
    # For binary classification
    if prediction[0] > 0.5:
        label = "Class 1 (e.g., Not Anime Face)"
    else:
        label = "Class 0 (e.g., Anime Face)"
    
    print(f"Prediction: {label}")

if name == "main":
    test_image = "test.jpg"  # Replace with your actual test image
    if os.path.exists(test_image):
        predict(test_image)
    else:
        print(f"❌ {test_image} not found. Place a test image in the same directory.")