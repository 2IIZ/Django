# @Date:   2019-01-03T11:02:15+01:00
# @Last modified time: 2019-01-03T16:00:49+01:00

"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# . -> root directory
from . import views

urlpatterns = [
	path('', views.home),
	#name='count' -> don't repeat yourself, used in form for action="" (home.html)
	#used for disassosiate the url
	path('count/', views.count, name='count'),

	path('goat', views.goat)
]
