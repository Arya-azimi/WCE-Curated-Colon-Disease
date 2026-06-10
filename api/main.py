from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io
from pydantic import BaseModel

app = FastAPI()

model = YOLO("../training/runs/classify/train/weights/best.pt")

# class names
classes = [
    "normal",
    "ulcerative_colitis",
    "polyps",
    "esophagitis"
]

@app.get("/")
def root():
    return {"message": "WCE Curated Colon Disease Detection API Running"}

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

@app.post("/predict",response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):

    # read image
    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # prediction
    results = model(image)

    probs = results[0].probs.data.tolist()

    predicted_index = probs.index(max(probs))

    predicted_class = classes[predicted_index]

    confidence = float(max(probs))

    return {
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2)
    }