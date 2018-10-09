""" Define preview URL. """

from django.conf.urls import patterns, url
from django.urls import path

from .views import preview

urlpatterns = [path('preview/$', preview, name='django_markdown_preview'),]
