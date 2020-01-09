from rest_framework import generics, views
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import UserSerializer
from tasks.models import Task

class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SingleUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

