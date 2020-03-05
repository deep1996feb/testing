from django.db import models

# Create your models here.
class Truth(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	salary=models.IntegerField()
	image=models.FileField(upload_to='images/',default="")
	class Meta:
		db_table='dare'
	
