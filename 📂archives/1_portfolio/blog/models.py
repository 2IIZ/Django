# @Date:   2019-01-04T09:54:48+01:00
# @Last modified time: 2019-01-06T00:24:49+01:00



from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=60)
	publication_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def __str__(self): #that show the particular object in admin section
		return self.title

	def summary(self):
		return self.body[:100] + "..." #return the first 100 char of the body string

	def publication_date_pretty(self):
		return self.publication_date.strftime('%B %e %Y')
