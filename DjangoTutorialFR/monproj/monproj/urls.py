"""monproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""
from django.urls import path 
from django.contrib import admin

from monsite.views import hello
from monsite.views import homepage
from monsite.views import books


urlpatterns = [
    path('', homepage),
    path('hello/', hello),
    path('books/', books),
    path('admin/', admin.site.urls),
]
