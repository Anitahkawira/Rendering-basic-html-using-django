from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.TextField()
    coarse = models.CharField(max_length = 200)
    year = models.IntegerField()
    def __str__ (self):
        return self.names