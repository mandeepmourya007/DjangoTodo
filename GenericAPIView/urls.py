from django.urls import path
from .views import create,read,update,delete,list_

urlpatterns = [
    path('create/', create.as_view()),
    path('read/<int:id>/', read.as_view()),
    path('update/<int:id>/', update.as_view()),
    path('delete/<int:id>/', delete.as_view()),
    path('list/', list_.as_view()),

]
