from django.urls import path
from .views import *


urlpatterns = [
    path('', Tasks.as_view(), name = 'main'),
    path('create_task/', CreateTask.as_view(), name = 'create'),
    path('update_task/<int:pk>', UpdateTask.as_view(), name = 'update'),
    path('delete_task/<int:pk>', DeleteTask.as_view(), name='delete'),
]