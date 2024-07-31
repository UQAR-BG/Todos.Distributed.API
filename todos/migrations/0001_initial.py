# Generated by Django 5.0.7 on 2024-07-29 17:51

import todos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_time', models.DateTimeField()),
                ('expiration_time', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Pending'), ('C', 'Completed'), ('E', 'Expired')], max_length=1, validators=[todos.models.validate_todo_status])),
            ],
        ),
    ]
