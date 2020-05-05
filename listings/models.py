from django.db import models
from realtors.models import Realtor
from django.dispatch import receiver
import os


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField(blank=False)
    bedrooms = models.IntegerField(blank=False)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=Listing)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.photo_main:
        if os.path.isfile(instance.photo_main.path):
            os.remove(instance.photo_main.path)
    if instance.photo_1:
        if os.path.isfile(instance.photo_1.path):
            os.remove(instance.photo_1.path)
    if instance.photo_2:
        if os.path.isfile(instance.photo_2.path):
            os.remove(instance.photo_2.path)
    if instance.photo_3:
        if os.path.isfile(instance.photo_3.path):
            os.remove(instance.photo_3.path)
    if instance.photo_4:
        if os.path.isfile(instance.photo_4.path):
            os.remove(instance.photo_4.path)
    if instance.photo_5:
        if os.path.isfile(instance.photo_5.path):
            os.remove(instance.photo_5.path)
    if instance.photo_6:
        if os.path.isfile(instance.photo_6.path):
            os.remove(instance.photo_6.path)


@receiver(models.signals.pre_save, sender=Listing)
def auto_delete_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_main
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_main
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_1
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_1
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_2
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_2
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_3
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_3
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_4
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_4
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_5
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_5
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    try:
        old_file = sender.objects.get(pk=instance.pk).photo_6
    except sender.DoesNotExist:
        return False
    new_file = instance.photo_6
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
