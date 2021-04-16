from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    hint = models.CharField(max_length=1000, blank=True, default=None)
    answer = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.auther.first_name + " " + self.auther.last_name + " - " + self.question