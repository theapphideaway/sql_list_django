from django.shortcuts import render
from .models import Item, Course, Student

# Create your views here.
def item_list(request):
	items = Item.objects.all()
	return render(request, 'item_list.html', {'items': items})  


def course_list(request):
	courses = Course.objects.all()
	return render(request, 'course_list.html', {'courses': courses})  

def course_details(request, id):
	course = Course.objects.filter(id=id).first()
	students = Student.objects.filter(course_id=id)
	return render(request, 'course_details.html', {'students': students, 'course': course})  