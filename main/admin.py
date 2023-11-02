from django.contrib import admin

from main.models import Profile, User

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "lastname", "email"]
    list_display_links = ["name", "lastname", "email"]    
