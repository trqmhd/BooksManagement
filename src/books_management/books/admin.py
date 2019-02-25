from django.contrib import admin
from .models import UserProfile, BookStore

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(BookStore)
