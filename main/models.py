from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    logo = models.FileField(upload_to="images/")
    title = models.CharField(max_length=50)
    full_title = models.CharField(max_length=250)
    slogan = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    phone = models.TextField(
        null=True,
        blank=True,
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_phone(self):
        if ";" in self.phone:
            return self.phone.split(";")
        return [self.phone]


class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    pfp = models.ImageField(upload_to='static/img')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Page.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.page.save()


class Appointment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


