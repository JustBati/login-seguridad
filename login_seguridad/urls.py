"""
URL configuration for login_seguridad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# login_seguridad/urls.py o myapp/urls.py

from django.urls import path, include
from myapp import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('main_page/', views.main_page_view, name='main_page'),
    path('add_machine/', views.add_machine, name='add_machine'),
    path('delete_machine/<int:id>/', views.delete_machine, name='delete_machine'),
    path('get_machines/', views.get_machines, name='get_machines'),
    path('loan_machine/', views.loan_machine, name='loan_machine'),
    path('get_loans/', views.get_loans, name='get_loans'),
]
