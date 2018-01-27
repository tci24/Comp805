from django.shortcuts import render

def home(request):
	"""
	Renders home page
	"""
	greeting = "uStudy - the best study site in the world"
	# a dictionary with a keyword our_greeting mapping to the variable greeting defined above.

	#first create variable with days of the week as a list
	days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
	'saturday', 'sunday']
	#then we add it to the template context
	context = {'our_greeting':greeting, 'weekday_list':days_of_week} #a dictionary
	return render(request, 'home.html', context)