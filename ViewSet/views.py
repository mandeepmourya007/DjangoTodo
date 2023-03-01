from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from function_based_view.models import Task
from GenericAPIView.serializer import TaskModelSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer


class ViewSet(viewsets.ViewSet):

    def list(self, request):
        print("******List******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        tasks = Task.objects.all()
        serializer = TaskModelSerializer(tasks, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        print("******Retrieve******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        id = pk
        if id is not None:
            tasks = Task.objects.get(id=id)
            serializer = TaskModelSerializer(tasks)
            return Response(serializer.data)

    def create(self, request):
        print("******Create******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        serializer = TaskModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": " Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        print("******Update******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        id = pk
        task = Task.objects.get(id=id)
        serializer = TaskModelSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Complete  Data Updated"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        print("******Partial Update******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        id = pk
        task = Task.objects.get(id=id)
        serializer = TaskModelSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial  Data Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        print("******Destroy******")
        print("Basename: ", self.basename)
        print("action: ", self.action)
        print("detail: ", self.detail)
        print("suffix: ", self.suffix)
        print("name: ", self.name)
        print("description: ", self.description)
        id = pk
        task = Task.objects.get(id=id)
        task.delete()
        return Response({"msg": " Deleted"}, status=status.HTTP_204_NO_CONTENT)
