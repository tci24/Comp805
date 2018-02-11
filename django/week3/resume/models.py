from django.db import models

# Create your models here.
class Experience(models.Model):
	title = models.CharField(max_length=60, null=False, blank=False)
	location = models.CharField(max_length=60, null=False, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	description = models.TextField(null=False, blank=True)

	def __str__(self):
		return self.title

class Education(models.Model):
	institution_name = models.CharField(max_length=60, null=False, 
		blank=False)
	location = models.CharField(max_length=60, null=False, blank=True)
	degree = models.CharField(max_length=60, null=False, blank=True)
	major = models.CharField(max_length=60, null=False, blank=True)
	gpa = models.FloatField(null=False, blank=True)

	def __str__(self):
		return self.institution_name