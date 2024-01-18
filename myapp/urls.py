# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main_page/', views.main_page_view, name='main_page'),
    path('add_machine/', views.add_machine, name='add_machine'),
    path('delete_machine/<int:id>/', views.delete_machine, name='delete_machine'),
    path('get_machines/', views.get_machines, name='get_machines'),
    path('loan_machine/', views.loan_machine, name='loan_machine'),
    path('get_loans/', views.get_loans, name='get_loans'),
    # ... otras URLs ...
]
