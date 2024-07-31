from django.db import models
from django.core.exceptions import ValidationError

from datetime import datetime

def validate_todo_status(value):
    if (value != "D" and value != "P" and value != "C" and value != "E"):
        raise ValidationError("The todo status must be 'D', 'P', 'C' or 'E'")

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    expiration_time = models.DateTimeField()
    description = models.CharField(max_length=500)
    TODO_STATUS = (("D", "Draft"), ("P", "Pending"), ("C", "Completed"), ("E", "Expired"))
    status = models.CharField(max_length=1, choices=TODO_STATUS, validators=[validate_todo_status], default="D")