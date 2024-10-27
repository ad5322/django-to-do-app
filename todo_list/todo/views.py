from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request,'The task was delted successfully')
        return super(TaskDelete,self).form_valid(form)
        
    

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        messages.success(self.request,'The task was updated successfully')
        return super(TaskUpdate,self).form_valid(form)
    


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request, 'the task created successfully')
        return super(TaskCreate,self).form_valid(form)
    
    

def home(request):
    return render(request,'home.html')

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'