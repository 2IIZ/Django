# @Date:   2019-01-03T11:34:37+01:00
# @Last modified time: 2019-01-03T15:49:43+01:00

#return some info into http response
from django.http import HttpResponse
from django.shortcuts import render

#every time someone come visit the page it will send this request
def home(request):
	#request, redirect to home.html, with a dictionary
	return render(request, 'home.html')

def count(request):
	#name='count' -> don't repeat yourself, used in form for action="" (home.html)
	#used for disassosiate the url
	return render(request, 'count.html', name='count')


def goat(request):
	#send a HttpResponse with html code inside
	#return HttpResponse("<h1>THIS IS GOAT VILLAGE !</h1>")
	return render(request, 'goathome.html', {'Welcome':'THIS IS GOAT VILLAGE !'})
