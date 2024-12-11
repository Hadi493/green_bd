from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    store_profile = models.ImageField(upload_to='store_profiles/')

    def __str__(self):
        return self.name

