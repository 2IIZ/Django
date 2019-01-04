# @Date:   2019-01-04T09:55:12+01:00
# @Last modified time: 2019-01-04T16:20:10+01:00



from django.shortcuts import render

# Create your views here.
# templates/jobs/.html
#	the engine automatically know where to found the /templates from the views.py-->
def home(request):
	return render(request, 'jobs/home.html')
