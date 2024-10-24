from django.urls import path
from . import views
from .views import home, TaskList
urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/',TaskList.as_view(),name='tasks'),
]