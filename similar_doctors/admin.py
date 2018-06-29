from django.contrib import admin

from .models import Doctor, Rating

admin.site.register(Doctor)
admin.site.register(Rating)