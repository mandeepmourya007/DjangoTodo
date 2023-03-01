from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import views

# Creating Router Object
router = DefaultRouter()

# Register ViewSet with Router
router.register('task', views.ViewSet, basename='task')
from ViewSet.views import testpage
urlpatterns = [
    path('', include(router.urls)),
]