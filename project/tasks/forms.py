from .models import Task
from django import forms
from django.forms import ValidationError
import re


class CreatTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("name", "description")

        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control", "id" : "Name", "placeholder" : "Название задачи"}),
            "description" : forms.TextInput(attrs={"class" : "form-control", "id" : "Description", "placeholder" : "Описание задачи"})
        }

class UpdateTaskForm(forms.ModelForm):

    class Meta:
        STATUS_TASK = [
            (True, 'Выполнено'),
            (False, 'Невыполнено')
        ]

        model = Task
        fields = ("name", "description", "status")

        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control", "id" : "Name", "placeholder" : "Название задачи"}),
            "description" : forms.TextInput(attrs={"class" : "form-control", "id" : "Description", "placeholder" : "Описание задачи"}),
            "status" : forms.Select(choices=STATUS_TASK, attrs={"class" : "form-control", "id" : "Status", "placeholder" : "Статус задачи"})
        }
