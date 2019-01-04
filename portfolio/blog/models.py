# @Date:   2019-01-04T09:54:48+01:00
# @Last modified time: 2019-01-04T15:38:07+01:00



from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=60)
	publication_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')
