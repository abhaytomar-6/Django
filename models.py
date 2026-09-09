
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    is_student = models.BooleanField(default=True)
    enrolled_courses = models.ManyToManyField('courses.Course', blank=True)
    
    def __str__(self):
        return self.username
