from django.db import models

# Create your models here.


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
