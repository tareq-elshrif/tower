from django.contrib import admin
from .models import Employees,Tower,Apartments,Tenants
# Register your models here.
admin.site.register(Employees)
admin.site.register(Tower)
admin.site.register(Apartments)
admin.site.register(Tenants)