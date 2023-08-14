from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

# Create your views here.

def index(request):
    return HttpResponse("This will be a text-to-image converter.")

def t2i(request):
    return HttpResponse("You requested an image.")

def get_text2image(request):
    API_URL = "https://api-inference.huggingface.co/models/devscion/pakhistoricalplaces"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(
        API_URL, headers=headers,
        json={
            "inputs": "Astronaut riding a horse",
        })
    image_bytes = response.content
    # You can access the image with PIL.Image for example
    # import io
    # from PIL import Image
    # image = Image.open(io.BytesIO(image_bytes))
    # #base string of image
    import base64
    base64_string = base64.b64encode(image_bytes)
    base64_string = base64_string.decode('utf-8')
    
    return JsonResponse({"image":base64_string})