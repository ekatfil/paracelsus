from django.contrib import admin

from main.models import Profile, Appointment

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

admin.site.register(Appointment)
