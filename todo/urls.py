from django.urls import path
from django.views.generic import TemplateView
from .views import TodoCreateView,TodoCurrentView

urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('create/',TodoCreateView.as_view(),name='create'),
    path('current/',TodoCurrentView.as_view(),name='current'),
]
