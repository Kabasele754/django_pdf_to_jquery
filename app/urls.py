from django.urls import path
from .views import home_pdf

urlpatterns = [
    path("", home_pdf)
    
]

