from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee

# Register models in Django Admin
admin.site.register(Employee)
