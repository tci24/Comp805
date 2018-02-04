"""
lab2.py
Tiffany
01/30/2018
"""
def squared(num_list):
	"""
	Squares numbers in num_list
	num_list: list of numbers
	Returns: list of these numbers squared
	"""

	new_list = [] #initialize list to hold result
	# iterate through num_list and square each element
	for num in num_list:
		sq_num = pow(num, 2)
		new_list.append (sq_num)
	return new_list

def check_title(title_list):
	"""
	Removes strings in title_list that have numbers and aren't title case
	title_list: list of strings
	Returns: list of strings that are titles
	"""

	new_list = []
	for item in title_list:
        item = str(item)
        if item[0].isupper() and not item.isdigit():
    		if item.istitle( ):
            	new_list.append(item)
    return new_list

def restock_inventory(inventory):
	"""
	Increases inventory of each item in dictionary by 10
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equeals the number of that item currently on hand
	Returns: updated dictionary where each inventory item is restocked
	"""
    dict = {}
    for item in inventory:
        if item in dict:
            dict[item] = dict[item] + 10
        else:
            dict[item] = inventory[item] + 10
    return dict

def filter_0_items(inventory):
	"""
	Removes items that have a value of 0 from a dictionary of inventories
	inventory: a dictionary with:
		key: string that is the name of the inventory item
		value: integer that equeals the number of that item currently on hand
	Returns: the same inventory_dict with any item that had 0 quantity removed
	"""
    for item in list(inventory.keys()):
        if inventory[item] == 0:
            del inventory[item]
    return inventory
