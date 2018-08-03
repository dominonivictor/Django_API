from django.urls import path, include
from . import views
from rest_framework import routers #this takes care of generating all url for the models

router = routers.DefaultRouter()
router.register('tasks', views.TaskView)

urlpatterns = [
    #path('', include('tasks.urls')),
    path('', include(router.urls)),
]
