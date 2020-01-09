from django.urls import path
from .views import TasksList, SingleTask

urlpatterns = [
    path('tasks/', TasksList.as_view()),
    path('tasks/<int:pk>/', SingleTask.as_view()),
]