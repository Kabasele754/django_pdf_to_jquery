from django.shortcuts import render
from .models import Article

# Create your views here.

def home_pdf(request, template_name= "index.html"):
    context = {}
    articles = Article.objects.all()
    context['articles'] = articles
    
    return render(request, template_name, context)