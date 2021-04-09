from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(verbose_name='Teacher', default=False)
    is_student = models.BooleanField(verbose_name='Student', default=False)
