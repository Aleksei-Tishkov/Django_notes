from django.db import models
from reg.models import User


class Note(models.Model):
    author = models.IntegerField(default=None)
    text = models.CharField(max_length=250, default=None)
