#!/usr/bin/env python3

from django.urls import path
from . import views

app_name = 'sqlist_app'

urlpatterns = [
	path('', views.item_list, name='item_list'),
	path('course/', views.course_list, name='course_list'),
	path('course/<int:id>', views.course_details, name='course_details')
	
]