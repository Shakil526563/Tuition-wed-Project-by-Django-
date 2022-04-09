from django.contrib import admin
from .models import Contact,guardian_info
# Register your models here.
admin.site.register(Contact)
admin.site.register(guardian_info)