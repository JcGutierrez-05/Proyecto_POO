"""
URL configuration for pro_miscelania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_cliente_view, name='crear_cliente'),
    path('creado/', lambda request: render(request, 'clientes/cliente_creado.html'), name='cliente_creado'),
]
    path('clientes/modificar/<str:email>/', views.modificar_cliente_view, name='modificar_cliente'),
    path('clientes/mostrar/<str:email>/', views.mostrar_cliente_view, name='mostrar_cliente'),
    path('clientes/eliminar/<str:email>/', views.eliminar_cliente_view, name='eliminar_cliente'),


urlpatterns = [
    path('admin/', admin.site.urls),
]
