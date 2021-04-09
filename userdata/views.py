from django.shortcuts import render
from .forms import CustomForm, TeacherForm
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import CustomUser


class CustomUserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = UserSerializer


def create_user(request):
    if request.method == 'GET':
        form = CustomForm()
    elif request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'userdata/create_user.html', context={'form': form})
