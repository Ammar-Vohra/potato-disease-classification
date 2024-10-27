from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
    'http://localhost:5000',  # Flask frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the Keras model
MODEL = tf.keras.models.load_model(r'C:\Users\ammar\OneDrive\Desktop\Techma Zone DS\Potato-Disease-Classification\saved_models\model.keras')
CLASS_NAMES = ['Potato Early', 'Potato Late', 'Healthy']

@app.get('/ping')
async def ping():
    return {"message": "Hello, I am alive"}

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize((224, 224))  # Resize if the model expects a specific size
    return np.array(image)

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    try:
        image = read_file_as_image(await file.read())
        image_batch = np.expand_dims(image, 0)  # Add batch dimension

        prediction = MODEL.predict(image_batch)
        predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
        confidence = np.max(prediction[0])

        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
