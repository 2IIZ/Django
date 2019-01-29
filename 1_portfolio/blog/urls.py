# @Date:   2019-01-05T21:57:30+01:00
# @Last modified time: 2019-01-06T00:28:16+01:00

from django.urls import path

from . import views

urlpatterns = [
	path('', views.allblogs, name="allblogs"), #will search the allblogs page of blog
	path('<int:blog_id>/', views.detail, name='detail'), #in url /blog/1.html
]
