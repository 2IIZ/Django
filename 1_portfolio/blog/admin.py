# @Date:   2019-01-04T09:54:47+01:00
# @Last modified time: 2019-01-04T15:23:45+01:00



from django.contrib import admin

# Register your models here.
from .models import Blog

admin.site.register(Blog)
