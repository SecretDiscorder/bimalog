"""
URL configuration for project project.

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
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('quran/', views.quran, name='quran'),

    path('', views.personal, name=""),
    path('project/', views.project, name="project"),
    path('profile/', views.profile, name="profile"),
    path('base/', views.base, name="base"),
    path('satuan/', views.satuan, name="satuan"),
    path('blang/', views.index, name="blang"),
    path('kalkulator/', views.kalkulator, name="kalkulator"),
    path('clock/',views.server_time,name="clock"),
    path('youtube/',views.youtube,name="youtube"),
    path('morse/',views.morse,name="morse"),
    path('prima/',views.prima,name="prima"),
    path('translator/',views.translator,name="translator"),
    path('probli/', views.probli, name='probli'),
    path('translate/', views.translate, name='translate'),
    path('translate/translate_ori/', views.search_original_coordinates, name='translate_ori'),
    path('translate/translate_end/', views.translated_search, name='translate_end'),
    path('aksara_converter/', views.aksara_converter, name='aksara_converter'),
    path('aksara_converter/aksara_converter_image/', views.convert_image, name='convert_image'),
]
