# @Date:   2019-01-03T11:34:37+01:00
# @Last modified time: 2019-01-03T11:40:02+01:00

#return some info into http response
from django.http import HttpResponse

#every time someone come visit the page it will send this request
def home(request):
	return HttpResponse("Hello")

def goat(request):
	return HttpResponse("<h1>THIS IS GOAT VILLAGE !</h1>")
