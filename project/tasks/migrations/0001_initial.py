# Generated by Django 4.2 on 2023-04-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
