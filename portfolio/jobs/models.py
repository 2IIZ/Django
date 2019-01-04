# @Date:   2019-01-04T09:55:12+01:00
# @Last modified time: 2019-01-04T10:13:21+01:00



from django.db import models

class Job(models.Model):
	image = models.ImageField(upload_to='images/') #every time someone upload a image, it will be upload to images/ folder
	summary = models.CharField(max_length=120)
