from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import *



class CreateTask(CreateView):
    form_class = CreatTaskForm
    model = Task
    success_url = reverse_lazy('main')
    template_name = 'tasks/create_task.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание новой задачи"
        return context
    
class Tasks(ListView):
    model = Task
    template_name = 'tasks/main.html'
    context_object_name = "tasks"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Список задач"
        return context

    def get_queryset(self):
        request = self.request.GET

        if request:

            if self.request.GET.get("status"):
                status = True if self.request.GET.get("status") == "Выполнено" else False
                return Task.objects.filter(status=status)
            
            if self.request.GET.get("order"):
                return Task.objects.all().order_by("-time_created")
            
        return Task.objects.all()
        


class UpdateTask(UpdateView):
    model = Task
    template_name = 'tasks/update_task.html'
    form_class = UpdateTaskForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Редактирование задачи"
        context["task_pk"] = self.request.path.split("/")[-1]
        return context
    

class DeleteTask(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('main')
    context_object_name = "task"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Удаление задачи"
        return context
