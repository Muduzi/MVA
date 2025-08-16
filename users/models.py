from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    User = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now=True)
    Options = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    Gender = models.CharField(null=True, choices=Options, max_length=8, default='Female')
    DOB = models.DateField(null=True)
    Photo = models.ImageField(null=True, upload_to='photo/profilePhoto', width_field=None, height_field=None)
    About = models.CharField(null=True, blank=True, max_length=200)
    Contact1 = models.CharField(null=True, blank=True,  max_length=15)
    Contact2 = models.CharField(null=True, blank=True, max_length=15)
    City = models.CharField(null=True, blank=True, max_length=50)
    Country = models.CharField(null=True, blank=True, max_length=50)
    Latitude = models.CharField(null=True, blank=True, max_length=200)
    Longitude = models.CharField(null=True, blank=True, max_length=200)
    Instagram = models.CharField(null=True, blank=True, max_length=100)
    Facebook = models.CharField(null=True, blank=True, max_length=100)
    X = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.User
