from django.db.models.signals import post_save # Signals get fired after the object get saved.
from django.contrib.auth.models import User # User = signal sender
from django.dispatch import receiver 
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): # kwargs means it accepts any additional keyword argument.
    instance.profile.save()