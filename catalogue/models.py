from django.db import models
from users.models import Profile
from django.core.validators import FileExtensionValidator
# Create your models here.


class CatalogueSection(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(null=False, blank=False, max_length=20)
    Photo = models.ImageField(null=True, blank=False, upload_to='photo/products', width_field=None, height_field=None)


class Video(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    Section = models.ForeignKey(CatalogueSection, on_delete=models.CASCADE, blank=True, null=True)
    Date = models.DateTimeField(auto_now=True)
    Title = models.CharField(null=False, max_length=20)
    Video = models.FileField(blank=False, null=False,
                             upload_to='videos/video',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'wmv',
                                                                                    'mkv', 'webm'])])
    Thumbnail = models.ImageField(null=False, upload_to='videos/thumbnails', width_field=None, height_field=None)
    Description = models.TextField(null=False, max_length=160, default='')

    def __str__(self):
        return self.Title


class Product(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    Section = models.ForeignKey(CatalogueSection, on_delete=models.CASCADE, blank=True, null=True)
    Date = models.DateTimeField(auto_now=True)
    Name = models.CharField(null=False, max_length=20)
    Price = models.IntegerField(null=False, default=0)
    Description = models.TextField(null=False, max_length=160)

    def __str__(self):
        return self.Name


class ProductPhoto(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=False)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    Photo = models.ImageField(null=False, upload_to='photo/products', width_field=None, height_field=None)


class ProductFeature(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=False)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False, null=False)
    Name = models.CharField(blank=False, null=False, max_length=20)
    Description = models.TextField(blank=False, null=False, max_length=100, default='')
