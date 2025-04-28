from django.urls import path
from . import views

urlpatterns = [
    path('api/companies', views.CompanyList.as_view(), name='companies_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/companies/<int:pk>', views.CompanyDetail.as_view(), name='companies_detail'), # api/contacts will be routed to the ContactDetail view for handling
]