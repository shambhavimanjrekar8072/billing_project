from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Billing)
admin.site.register(models.Course)	
admin.site.register(models.Subject)
admin.site.register(models.User)