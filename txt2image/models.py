from django.db import models

# Create your models here.
class GeneratedImages(models.Model):
    image = models.ImageField(upload_to="images/")
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)