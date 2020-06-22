from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.

def user_list(request):
    context = {'user_list':User.objects.all()}
    return render(request, 'user_register/user_list.html', context)

def user_form(request, id = 0):
    if request.method == "POST":
        if id == 0:
            form = UserForm(request.POST)
        else:
            user = User.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/user/list')
            
    else:
        if id == 0: # "if id == 0" -> its create operation
            form = UserForm()
        else:
            user = User.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, 'user_register/user_form.html', {'form':form})


def user_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('/user/list')
