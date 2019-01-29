from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        # button signup pressed
        if request.POST['password'] == request.POST['confirmPassword']:
            try:
                user = User.objects.get(username = request.POST['email'])
                return render(request, 'accounts/signup.html', {'error':'email already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['email'], password = request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'password must match'})
    else:
        #just the url that pop
        return render(request, 'accounts/signup.html')

def login(request):
    # check if is a post
    if request.method == 'POST':
        # verify if there's a match with the sended and the bdd
        user = auth.authenticate(username = request.POST['email'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'The user or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
