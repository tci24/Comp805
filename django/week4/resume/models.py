from django.db import models

# Create your models here.

class Resume(models.Model):
	first_name = models.CharField(max_length=25, null=False, blank=False)
	last_name = models.CharField(max_length=25, null=True, blank=True)

	def get_full_name(self):
		return "{} {}".format(self.first_name, self.last_name)

	def __str__(self):
		return self.last_name


class Experience(models.Model):
	parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
	title = models.CharField(max_length=60, null=False, blank=False)
	location = models.CharField(max_length=60, null=False, blank=True)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	description = models.TextField(null=False, blank=True)

	def __str__(self):
		return self.title

class Education(models.Model):
	parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
	institution_name = models.CharField(max_length=60, null=False, 
		blank=False)
	location = models.CharField(max_length=60, null=False, blank=True)
	degree = models.CharField(max_length=60, null=False, blank=True)
	major = models.CharField(max_length=60, null=False, blank=True)
	gpa = models.FloatField(null=False, blank=True)

	def __str__(self):
		return self.institution_name