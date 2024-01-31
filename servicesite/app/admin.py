from django.contrib import admin

# Register your models here.
from .models import *

class Admincontact_details(admin.ModelAdmin):
    list_display = ['name','email','mobile','message']


admin.site.register(contact_details,Admincontact_details)