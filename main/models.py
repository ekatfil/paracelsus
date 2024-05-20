from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    """Основная информация"""

    title = models.CharField("Заголовок сайта", max_length=50)

    slogan = models.TextField(
        "Слоган",
        max_length=100,
        null=True,
        blank=True,
    )

    description = models.TextField(
        "Описание",
        max_length=700,
        null=True,
        blank=True,
    )

    img = models.FileField("Главная картинка")

    def __str__(self):
        return f"{self.title}"


class Page(models.Model):

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name="profile")
    # last_name = models.CharField(max_length=155)
    # first_name = models.CharField(max_length=155)
    patronymic = models.CharField(max_length=155, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    snils = models.PositiveIntegerField(
                validators=[MinValueValidator(100_000_000_00),
                            MaxValueValidator(999_999_999_99)],
                null=True,
                blank=True,)

    pfp = models.ImageField(upload_to='static/img', blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    profession = models.CharField(max_length=155, blank=True, null=True)
    education = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"
    
    class Meta:
        verbose_name = "Профиль пользователей"
        verbose_name_plural = "Профили пользователй"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Page.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


CATEGORY_APPOINTMENT = (
    ("Личное", "Личное"), ("Лекарства", "Лекарства")
)


class Appointment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateField()
    time = models.TimeField(blank=True, null=True)
    category = models.CharField(max_length=155,
                                choices=CATEGORY_APPOINTMENT,
                                default="Личное")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.day} {self.user}"


class GroupDoctor(models.Model):
    users = models.ManyToManyField(User, related_name="groups_doctor")
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title
