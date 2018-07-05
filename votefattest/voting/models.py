from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    @property
    def image_url(self):
        return self.image.name

    def __str__(self):
        return self.user.get_full_name()


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
