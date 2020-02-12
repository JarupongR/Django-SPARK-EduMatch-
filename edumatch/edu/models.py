from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,default=None)
    name = models.TextField(default='',blank=True)
    gender = models.TextField(default='',blank=True)
    city = models.TextField(default='',blank=True)
    expert = models.TextField(default='',blank=True)

    def __str__(self):
        return self.name
    
class Selected_Subject(models.Model):
    subject = models.TextField(default='')


