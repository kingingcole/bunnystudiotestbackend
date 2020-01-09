from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.serializer import TaskSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username' ,'tasks']