from django.shortcuts import render

# Create your views here.
def scriptFun(request):
    return render(request, 'script/home.html')
