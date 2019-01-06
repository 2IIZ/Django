# @Date:   2019-01-04T09:54:48+01:00
# @Last modified time: 2019-01-06T20:41:32+01:00



from django.shortcuts import render, get_object_or_404


from .models import Blog
# Create your views here.
def allblogs(request):
	blogs = Blog.objects #retrieve
	return render(request, 'blog/allblogs.html', {"blogs":blogs}) #pass


def detail(request, blog_id):
	detailblog = get_object_or_404(Blog, pk=blog_id) #will search or fail, in Blog db with the primary key of the /blog/>id<.html
	return render(request, 'blog/detail.html', {'blog':detailblog})

#1 import blog
#2 retrieve data and pass data to the html with a dictionary
#3 add it to the html page with {{ blog.title }}
