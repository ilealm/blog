from django.urls import path
# from .views import HomePageView, BlogPageView
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
    # path('blog/',BlogPageView.as_view(), name='blog')