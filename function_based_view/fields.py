from django.db import models

class TaskStatus(models.IntegerChoices):
    PENDING = 10, "Pending"
    COMPETLED = 20, "Completed"
    CANCELLED = 30,"Cancelled"
