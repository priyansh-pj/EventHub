from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def createProfile(sender, instance, **kwargs):
    if kwargs['created']:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )

@receiver(post_delete, sender=Profile)
def deleteProfile(sender,instance,**kwargs):
    profile = instance.user
    profile.delete()
    print('user deleted')

