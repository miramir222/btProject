from django.db import models
from django.dispatch import receiver
import os
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
@receiver(models.signals.post_delete, sender=Realtor)
def auto_delete_file_on_delete(sender, instance,**kwargs):
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
@receiver(models.signals.pre_save, sender=Realtor)
def auto_delete_on_file_change(sender, instance, ** kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).photo
    except sender.DoesNotExist:
        return False
    new_file = instance.photo
    if not new_file == old_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    
        