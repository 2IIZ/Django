# @Date:   2019-01-04T09:55:12+01:00
# @Last modified time: 2019-01-04T10:47:29+01:00

# This page is for "we want to show up which models the admin can see"

from django.contrib import admin

# Register your models here.
from .models import Job

admin.site.register(Job)
