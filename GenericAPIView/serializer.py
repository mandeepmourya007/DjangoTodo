
from rest_framework import serializers
from function_based_view.models import Task


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
