from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    #.ModelSerializer will show you relevant info to the models
    #can create new models, update it
    class Meta:
        model = Task
        fields = ('id', 'name', 'deadline', 'details')
