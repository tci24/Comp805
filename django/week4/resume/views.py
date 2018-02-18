"""
portfolioplus/resume/views.py for the resume app in portfolioplus
Tiffany
02/10/2018
"""

from django.shortcuts import render
from .models import Resume, Experience, Education

# Create your views here.
def home(request):
	"""
	Returns the resume app resume template.
	"""
	r1 = Resume.objects.first()
	context = {'my_resume': r1}
	return render(request, 'resume/resume.html', context)