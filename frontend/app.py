from flask import Flask, render_template, request, url_for
import requests
from PIL import Image
import os

app = Flask(__name__)

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    
    # Define a path to save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    image = Image.open(file)
    image.save(file_path)

    # Send image file to FastAPI server for prediction
    with open(file_path, 'rb') as img_file:
        response = requests.post('http://localhost:8000/predict', files={'file': img_file})
    prediction = response.json()

    # Pass prediction and file path (relative to static folder) to the template
    return render_template('index.html', prediction=prediction, image_path=file.filename)

if __name__ == "__main__":
    app.run(debug=True)