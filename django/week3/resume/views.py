"""
portfolioplus/resume/views.py for the resume app in portfolioplus
Tiffany
02/10/2018
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('Welcome to the resume app')