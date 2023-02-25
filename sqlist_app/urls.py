#!/usr/bin/env python3

from django.urls import path
from . import views

app_name = 'sqlist_app'

urlpatterns = [
	path('', views.item_list, name='item_list')
]