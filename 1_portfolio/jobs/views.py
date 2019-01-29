# @Date:   2019-01-04T09:55:12+01:00
# @Last modified time: 2019-01-04T17:00:47+01:00



from django.shortcuts import render

from .models import Job

# templates/jobs/.html
#	the engine automatically know where to found the /templates from the views.py-->
def home(request):
	jobs = Job.objects #will retrieve all data from the job database
	return render(request, 'jobs/home.html', {"jobs":jobs})
