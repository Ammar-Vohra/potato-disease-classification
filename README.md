Potato Disease Classification
This project is a deep learning-based web application that classifies potato leaf diseases, using a trained model to recognize and categorize images as "Potato Early," "Potato Late," or "Healthy." The application consists of a FastAPI server for model inference and a Flask frontend that allows users to upload leaf images, view predictions, and see the classification results in an easy-to-use interface.

Project Structure
project_folder/
├── api/
│   ├── main.py                # FastAPI server
│   └── requirements.txt       # Python dependencies for FastAPI
├── app.py                     # Flask server
├── model/                     # Trained Keras model
├── notebooks/                 # Jupyter notebooks for EDA and model training
├── dataset/                   # Dataset used for training (optional, not included in the repo)
├── templates/
│   └── index.html             # HTML template for Flask frontend
└── static/
    ├── bg.png                 # Background image for the web page
    └── styles.css             # Styling for the application


Features
FastAPI Backend: Handles image classification and returns prediction results.
Flask Frontend: User-friendly interface for image upload and result display.
Model: Trained deep learning model using TensorFlow/Keras, designed to detect and classify leaf diseases.

Setup Instructions
Prerequisites
Python 3.7+
Pipenv or venv for virtual environment management

Installation
1. Clone the Repository:
git clone https://github.com/yourusername/potato-disease-classification.git
cd potato-disease-classification

2. Create Virtual Environment:
python -m venv .venv
source .venv/bin/activate  # For MacOS/Linux
.venv\Scripts\activate     # For Windows

3. Install Dependencies:
Install required packages for both FastAPI and Flask
pip install -r api/requirements.txt
pip install -r requirements.txt

4. Run FastAPI Backend:
In one terminal, navigate to the api folder and start the FastAPI server:
cd api
uvicorn main:app --reload

5. Run Flask Frontend:
Open a new terminal, navigate to the main project folder, and start the Flask server:
python app.py

Usage
1. Open a web browser and go to http://localhost:5000.
2. Upload an image of a potato leaf to classify.
3. View the prediction results displayed on the page.

Technical Details
1. Model: A CNN model trained on a dataset of potato leaves to identify common diseases and healthy leaves.
2. API: FastAPI handles the backend logic and model inference, while Flask manages the frontend and interacts with FastAPI for predictions.
3. Image Processing: Uploaded images are resized and pre-processed to fit the model’s input requirements.

License
This project is licensed under the MIT License - see the LICENSE file for details.