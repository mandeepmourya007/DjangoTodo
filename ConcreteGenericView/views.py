from rest_framework import generics
from function_based_view.models import Task
from GenericAPIView.serializer import TaskModelSerializer


class create(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class read(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class update(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class delete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class list_(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class RetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class RetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class ListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
