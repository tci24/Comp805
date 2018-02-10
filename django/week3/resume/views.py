"""
portfolioplus/resume/views.py for the resume app in portfolioplus
Tiffany
02/10/2018
"""

from django.shortcuts import render
from .models import Experience

# Create your views here.
def home(request):
	"""
	Returns the resume app resume template.
	"""
	qs_exp = Experience.objects.all()
	context = {'my_experience': qs_exp}
	return render(request, 'resume/resume.html', context)