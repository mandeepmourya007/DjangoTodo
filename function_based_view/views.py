from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, JsonResponse
# Create your views here.



def create(request):
    if request.method=="POST":
        try:
            name = request.POST.get("name")
            detail = request.POST.get("detail")
            instance=Task.objects.create(name=name, detail=detail)
            return HttpResponse(f"Task Created with name {name} and id {instance.id}")
        except Exception as e:
            raise Exception(f"error {repr(e)} occured while creating task")
    return HttpResponse("not a valid request")
           

def read(request,id):
    instance= Task.objects.filter(id=id).values()
    return HttpResponse(instance)

def update(request,id):
    instance= Task.objects.get(id=id)
    instance.name = request.POST.get("name",instance.name)
    instance.detail = request.POST.get("detail",instance.detail)
    instance.task_status = request.POST.get("task_status",instance.task_status)
    instance.save()
    return HttpResponse(f"{instance} updated")

def delete(request,id):
    instance= Task.objects.get(id=id)
    instance.delete()
    return HttpResponse("task data deleted")

def list_(request):
    instances = list(Task.objects.all().values())
    return JsonResponse(instances,safe=False)