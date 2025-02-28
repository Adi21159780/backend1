from django.contrib import admin

# Register your models here.
from .models import Employee  # Import Employee model

admin.site.register(Employee)  # Register Employee in admin