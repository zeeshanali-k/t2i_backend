
from django.urls import path

from . import views

urlpatterns = [
    path("", views.t2i, name="index"),
    path("get_text2image", views.get_text2image, name="get_data"),
]