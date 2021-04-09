from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(verbose_name='Teacher', default=False)
    is_student = models.BooleanField(verbose_name='Student', default=False)


class Teacher(models.Model):
    teacher_since = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username


class Student(models.Model):
    date_of_birth = models.DateField(null=True, blank=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username
