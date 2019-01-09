from django.urls import path
from . import views

urlpatterns = [
    # "views.index" -> here i'm calling the function in polls/views.py
    path('', views.index, name="index")
]
