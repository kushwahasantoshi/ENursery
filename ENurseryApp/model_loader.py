import tensorflow as tf
import numpy as np
from PIL import Image

# Load MobileNetV2 from TensorFlow Hub
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# Function to preprocess image
def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))  # Resize to model input size
    img_array = np.array(img) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array