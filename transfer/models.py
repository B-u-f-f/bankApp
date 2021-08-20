from django.db import models
from django.urls import reverse
# Create your models here.

class CustomerAccount(models.Model):
    customer_acc_number = models.CharField(max_length=20, primary_key = True)
    customer_name = models.CharField(max_length=60)
    customer_email = models.EmailField()
    customer_balance = models.IntegerField()

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse('home_page')
