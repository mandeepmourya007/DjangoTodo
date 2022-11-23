from django.urls import path
from .views import create,read,update,delete,list_

app_name = "function_based_view"


urlpatterns =[
    path('create/', create ),
    path('read/<int:id>/', read),
    path('update/<int:id>/',update ),
    path('delete/<int:id>/', delete),
    path('list/',list_ ),

]