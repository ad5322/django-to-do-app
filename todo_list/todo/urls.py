from django.urls import path
from . import views
from .views import (
    home, 
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    )

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task/create/',TaskCreate.as_view(),name='task-create'),
    path('task/update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
]