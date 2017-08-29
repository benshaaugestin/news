from django.contrib import admin

from .models import News,Category,Profile

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Profile)