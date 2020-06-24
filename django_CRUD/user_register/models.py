from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class User(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)