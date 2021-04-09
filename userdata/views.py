from django.shortcuts import render
from .forms import CustomForm, TeacherForm
from django.http import HttpResponseRedirect


def create_user(request):
    if request.method == 'GET':
        form = CustomForm()
    elif request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request, 'userdata/create_user.html', context={'form': form})
