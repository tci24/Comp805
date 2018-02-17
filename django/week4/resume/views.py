"""
portfolioplus/resume/views.py for the resume app in portfolioplus
Tiffany
02/10/2018
"""

from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def home(request):
	"""
	Returns the resume app resume template.
	"""
	qs_exp = Experience.objects.all()
	qs_edu = Education.objects.all()
	context = {'my_experience': qs_exp, 'my_education': qs_edu}
	return render(request, 'resume/resume.html', context)