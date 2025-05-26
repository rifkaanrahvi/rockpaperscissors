from flask import Flask, request, jsonify
from flask_cors import CORS # Tambahkan ini
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import io
import os

app = Flask(__name__)
CORS(app) # Tambahkan ini SETELAH `app = Flask(__name__)`

# Load your trained model
# Make sure the model path is correct relative to app.py
MODEL_PATH = 'model_checkpoints/best_model.weights.h5'
model = None
try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# Define your class names based on your training data
CLASS_NAMES = ['paper', 'rock', 'scissors']
IMG_SIZE = (224, 224)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            img = load_img(io.BytesIO(file.read()), target_size=IMG_SIZE)
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = CLASS_NAMES[predicted_class_index]
            probabilities = predictions[0].tolist()

            return jsonify({
                'predicted_class': predicted_class_name,
                'probabilities': dict(zip(CLASS_NAMES, probabilities))
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Something went wrong during prediction'}), 500

if __name__ == '__main__':
    os.makedirs('model_checkpoints', exist_ok=True)
    app.run(debug=True)