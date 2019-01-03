# @Date:   2019-01-03T11:34:37+01:00
# @Last modified time: 2019-01-03T11:49:54+01:00

#return some info into http response
from django.http import HttpResponse
from django.shortcuts import render

#every time someone come visit the page it will send this request
def home(request):
	#request, redirect to home.html, with a dictionary
	return render(request, 'home.html', {'Welcome':'Welcome to the home page !'})

def goat(request):
	#send a HttpResponse with html code inside
	return HttpResponse("<h1>THIS IS GOAT VILLAGE !</h1>")
