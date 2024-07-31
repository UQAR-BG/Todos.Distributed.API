from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("expiration_time", "description", "status")

class TodoDtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "creation_time", "expiration_time", "description", "status")