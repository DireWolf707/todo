from django.urls import path
from django.views.generic import TemplateView
from .views import TodoCreateView,TodoCurrentView,TodoUpdateview,todo_complete,todo_delete,TodoCompleteView

urlpatterns = [
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('create/',TodoCreateView.as_view(),name='create'),
    path('current-todos/',TodoCurrentView.as_view(),name='current'),
    path('completed-todos/',TodoCompleteView.as_view(),name='completed_todos'),
    path('todo/<int:pk>/edit',TodoUpdateview.as_view(),name='update_view'),
    path('todo/<int:pk>/complete',todo_complete.as_view(),name='complete'),
    path('todo/<int:pk>/delete',todo_delete.as_view(),name='delete'),
]
