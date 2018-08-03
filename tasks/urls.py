from django.urls import path, include
from . import views
from rest_framework import routers #this takes care of generating all url for the models

#router will handle all of our urls for tasks
router = routers.DefaultRouter()
router.register('tasks', views.TaskView)

urlpatterns = [
    path('', include(router.urls)),
]
