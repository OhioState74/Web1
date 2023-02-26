"""Web1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from firstapp import views
from django.urls import re_path
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.index, name='home'),
    # # path('admin/', admin.site.urls),
    # # re_path(r'^about/contact',views.contact),
    # re_path(r'^about', views.about),
    # re_path(r'^contact', views.contact),
    # # re_path(r'^products/ (?P<productid>\d+)/', views.products),
    # # re_path(r'^users/ (?P<id>\d+) / (?P<name>\D+)/', views.users),
    # # re_path(r'^products/$', views.products),
    # path('products/<int:productid>/', views.products),
    # # path('users/<int:id>/<name>/', views.users),
    # path('products/', views.products),
    # path('users/', views.users),

    # переадресация
    path('', views.index),
    # path("about/", views.about),
    # path('contact/', views.contact),
    path('details/', views.details),
    # обращатся на прямую
    path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
                                          extra_context={"work": "Разработка програмных продуктов"})),
    path('index_app1/', views.index_app1),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),

]