from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100,default="python")
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.name