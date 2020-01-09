from django.urls import path
from .views import UsersList, SingleUser

urlpatterns = [
    path('users/', UsersList.as_view()),
    path('users/<str:username>/', SingleUser.as_view()),
]