from .views import DetailView
from django.urls import path

urlpatterns = [
    path('check/', DetailView.as_view()),
    ]