from django.contrib import admin
from .models import *

# Register your models here.

# class PersonAdmin(admin.ModelAdmin):

# class MusicianAdmin(admin.ModelAdmin):

admin.site.register(Person)
admin.site.register(Musician)
admin.site.register(Album)
