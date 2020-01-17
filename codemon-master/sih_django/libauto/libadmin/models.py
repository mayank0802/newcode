from django.db import models
import datetime
class book_info(models.Model):
	book_id = models.AutoField(primary_key = True)
	book_name = models.CharField(max_length = 50)
	book_author = models.CharField(max_length = 50)
	bk_student_id = models.IntegerField(default = -1)
	book_submission = models.DateField(default=datetime.date.today)
	book_issue = models.DateField(default=datetime.date.today)
	book_lot = models.CharField(default = '0' , max_length = 30)
	def __str__(self): 
		return self.book_name
class lib_admin(models.Model):
	a_id = models.AutoField(primary_key=True)
	a_name = models.CharField(max_length=50)
	a_phone = models.IntegerField()
	a_email = models.CharField(max_length = 50)	
	a_password = models.CharField(max_length = 60)
	def __str__(self): 
		return self.a_name	
class notice(models.Model):
	notice1 = models.CharField(max_length = 300)