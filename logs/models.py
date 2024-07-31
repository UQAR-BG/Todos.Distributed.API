from django.db import models
from django.core.exceptions import ValidationError

from datetime import datetime

def validate_log_level(value):
    if (value != "I" and value != "W" and value != "E" and value != "C"):
        raise ValidationError("The todo status must be 'I', 'W', 'C' or 'E'")

# Create your models here.
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    message = models.TextField()
    LOG_LEVEL = (("I", "Information"), ("W", "Warning"), ("E", "Error"), ("C", "Critical"))
    level = models.CharField(max_length=1, choices=LOG_LEVEL, validators=[validate_log_level])