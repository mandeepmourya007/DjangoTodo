from function_based_view.models import Task
from .serializer import TaskModelSerializer
from rest_framework import generics

from rest_framework import mixins


class create(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class read(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class update(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class delete(generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class list_(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
