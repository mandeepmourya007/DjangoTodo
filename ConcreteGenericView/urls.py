from django.urls import path
from .views import (
    create,
    read,
    update,
    delete,
    list_,
    RetrieveUpdate,
    RetrieveDestroy,
    ListCreate,
    RetrieveUpdateDestroy,
)

# here pk is default agrument name  if you want to give your own name you have to give lookup_field in class
urlpatterns = [
    path("create/", create.as_view()),
    path("read/<int:pk>/", read.as_view()),
    path("update/<int:pk>/", update.as_view()),
    path("delete/<int:pk>/", delete.as_view()),
    path("list/", list_.as_view()),
    path("retrieve-update/<int:pk>/", RetrieveUpdate.as_view()),
    path("retrieve-destroy/<int:pk>/", RetrieveDestroy.as_view()),
    path("list-create/", ListCreate.as_view()),
    path("retrieve-update-destroy/<int:pk>/", RetrieveUpdateDestroy.as_view()),
]
