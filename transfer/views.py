from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from .models import CustomerAccount, CustomerTransaction

from datetime import datetime
# Create your views here.

class HomepageView(TemplateView):
    template_name = 'home.html'


class UserAccountCreate(CreateView):
    model =  CustomerAccount
    template_name = 'createuser.html'

    fields = ['customer_acc_number', 'customer_name', 'customer_email', 'customer_balance']


class CustomerList(ListView):
    model = CustomerAccount
    template_name = 'customers.html'

    context_object_name = 'customers'

class TransferMoney(TemplateView):
    template_name = 'transfer.html'

class ProcessTransfer(TemplateView):
    template_name = 'process.html'
    context_object_name = 'outcome'
   
    isValid = None
    to = None
    fr = None
    a = None

    def dispatch(self, *args, **kwargs):
        self.to = self.request.GET['toAcc']
        self.fr = self.request.GET['fromAcc']
        self.a = int(self.request.GET['amount'])
        
        try:
            fromAccount = CustomerAccount.objects.get(customer_acc_number = self.fr)
            toAccount = CustomerAccount.objects.get(customer_acc_number = self.to)
            
            if(fromAccount.customer_balance >= self.a):
                self.isValid = True
                fromAccount.customer_balance -= self.a
                toAccount.customer_balance += self.a
                
                CustomerTransaction.objects.create(customer_to_acc_number = toAccount.customer_acc_number, \
                                                   customer_from_acc_number = fromAccount.customer_acc_number,\
                                                   transaction_time = str(datetime.now())) 
            else:
                self.isValid = False

            fromAccount.save()
            toAccount.save()
        except:
            self.isValid = False
    
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid'] = self.isValid
        
        return context
