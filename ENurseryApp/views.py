from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .model_loader import model, preprocess_image
import numpy as np


def Welcome(request):
    return HttpResponse("Hello World")


def predict_disease(request):
    if request.method == "POST" and request.FILES["leaf_image"]:
        image = request.FILES["leaf_image"]
        
        # Save uploaded image
        fs = FileSystemStorage()
        file_path = fs.save(image.name, image)
        img_array = preprocess_image(fs.path(file_path))

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)  # Get highest probability class

        # Map class index to disease name (You need to add a mapping dictionary)
        class_labels = {0: "Healthy", 1: "Bacterial Spot", 2: "Late Blight"}
        disease_name = class_labels.get(predicted_class, "Unknown")

        return render(request, "result.html", {"disease": disease_name})

    return render(request, "prediction.html")

