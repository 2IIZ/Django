from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    pub_date = models.DateTimeField()
    total_votes = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()

    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self): #that show the particular object in admin section
    	return self.title
