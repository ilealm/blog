# from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here. This is the regular views
class HomePageView(TemplateView):
    template_name = 'home.html'

class BlogPageView(ListView):
    template_name = 'blog.html'
    model = Post