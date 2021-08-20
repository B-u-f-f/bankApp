from django.urls import path

from .views import HomepageView, UserAccountCreate, CustomerList, TransferMoney, ProcessTransfer

urlpatterns = [
    path('', HomepageView.as_view(), name = 'home_page'),
    path('usercreate/', UserAccountCreate.as_view(), name = 'usercreate'),
    path('customerlist/', CustomerList.as_view(), name = 'customerlist'),
    path('transferMoney/', TransferMoney.as_view(), name = 'transfermoney'),
    path('processTransfer/', ProcessTransfer.as_view(), name = 'processtransfer')
]


