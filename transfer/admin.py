from django.contrib import admin
from .models import CustomerAccount, CustomerTransaction

# Register your models here.
 
admin.site.register(CustomerAccount)
admin.site.register(CustomerTransaction)

