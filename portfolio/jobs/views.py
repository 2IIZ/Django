# @Date:   2019-01-04T09:55:12+01:00
# @Last modified time: 2019-01-04T16:09:33+01:00



from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'jobs/home.html')
