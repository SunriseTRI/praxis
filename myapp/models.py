from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


#! useers
class Session(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    def __str__(self):
        return f"{self.name} - {self.date}"

#! мамберсы
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='p-photo/')

    def __str__(self):
        return self.name


class TeamInfo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='t-photo/')
    description = models.TextField()

    def __str__(self):
        return self.name