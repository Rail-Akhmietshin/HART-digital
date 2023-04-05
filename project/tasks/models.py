from django.db import models
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название задачи")
    description = models.TextField("Описание задачи")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
         return reverse('update', kwargs = {'pk' : self.pk})