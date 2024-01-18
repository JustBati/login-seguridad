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

from django.urls import path
from .views import login_view  # Asegúrate de importar la vista correctamente

urlpatterns = [
    # ... otras URLs ...
    path('login/', login_view, name='login'),
    path('main_page/', main_page_view, name='main_page'),  # Asegúrate de tener una vista para la página principal
]
