from django.contrib import admin

from .models import Item, Course, Student

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ['_id', 'title']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ['id', 'title']
	
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['id', 'course_id', 'name']
	