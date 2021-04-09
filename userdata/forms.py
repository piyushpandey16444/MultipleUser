from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Teacher, Student


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class CustomForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2',
                  'is_teacher', 'is_student')
