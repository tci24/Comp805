"""
lab3.py
Tiffany
02/06/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared

	>>> squared([1, 2, 3])
	[1, 4, 9]
	>>> squared([-1, -2])
	[1, 4]
	"""

	new_list = [] #initialize list to hold result
	# iterate through num_list and square each element
	for num in num_list:
		sq_num = pow(num, 2)
		new_list.append(sq_num)
	return new_list

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and aren't title case
	title_list: list of strings
	Returns: list of strings that are titles

	>>> check_title(['Hi', 'puppy', 'Dog'])
	['Hi', 'Dog']
	"""

	new_list = [ ]
	'''
	for title in title_list:
		if title.istitle( ) and title.isalpha( ):
				new_list.append(title)
	'''
	return new_list

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equeals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	
	>>> restock_inventory({'cherry':30, 'lemon':5})
	{'cherry':40, 'lemon':15}
	"""
	
	new_inventory = { }
	'''
	for key, val in inventory.items( ):
		new_inventory[key] = val + 10
	'''
	return new_inventory

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equeals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed

	>>> filter_0_items({'cherry':30, 'lemon':5, 'pear':0})
	{'cherry':30, 'lemon':5}
	"""

	new_inventory = { }
	'''
	for k, v in inventory.items( ):
		if v != 0:
			new_inventory[k] = v
	'''
	return new_inventory

def average_grades(grades):
	"""
	Takes grade values from a dictionary and averages them into a final grade
	grades: a dictionary of grades with:
		key: string of student names
		value: list of integer grades received in class
	Returns: dictionary that averages out the grades of each student
	
	>>> average_grades({'Michael':[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]})
	{'Josh':87.0, 'Daniel':79.0, 'Michael':89.0}
	"""

	new_grades = { }
	'''
	for student_name, student_grades in grades.items( ):
		new_grades[student_name] = sum(student_grades)/len(student_grades)
	'''
	return new_grades

if __name__ =='__main__':
	import doctest
	doctest.testmod( )
