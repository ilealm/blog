# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here. This is the regular views
class HomePageView(ListView):
    template_name = 'home.html'
    model = Post

