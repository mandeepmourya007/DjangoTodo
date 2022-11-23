from django.db import models
from .fields import TaskStatus
# Create your models here.

class Task(models.Model):
    name =  models.CharField(max_length=255)
    task_status = models.PositiveIntegerField("task status",choices=TaskStatus.choices,default=10) 
    detail = models.TextField()   
    

    class Meta:
        verbose_name = ("task")
        verbose_name_plural = ("tasks")
        

    def __str__(self):
        return self.name