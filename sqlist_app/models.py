from django.db import models

# Create your models here.

class Item(models.Model):
	_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 180)