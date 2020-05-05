from django.db import models
from listings.models import Listing
from django.contrib.auth.models import User
# Create your models here.
class Contact (models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=16)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name