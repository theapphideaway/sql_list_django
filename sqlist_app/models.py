from django.db import models

# Create your models here.

class Item(models.Model):
	_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 180)
	
class Course(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 180)
	
class Student(models.Model):
	id = models.AutoField(primary_key=True)
	course_id = models.CharField(max_length = 180)
	name = models.CharField(max_length = 180)
	