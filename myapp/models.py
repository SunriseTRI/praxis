from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Session(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    def __str__(self):
        return f"{self.name} - {self.date}"