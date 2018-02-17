"""
test_lab4.py
Tiffany
02/13/2018
"""

import unittest

class Lab4Test(unittest.TestCase):
	def test_squared(self):
		"""
		Tests lab4.squared()
		"""
		func = lab4.squared
		case1 = [1, 2, 3]
		expected1 = [1, 4, 9]
		self.assertEqual(func(case1), expected1)

	def test_check_title(self):
		"""
		Tests lab4.check_title()
		"""
		func = lab4.check_title
		case1 = ['Hi', 'puppy', 'Dog']
		expected1 = ['Hi', 'Dog']
		self.assertEqual(func(case1), expected1)

	def test_restock_inventory(self):
		"""
		Tests lab4.restock_inventory()
		"""
		func = lab4.restock_inventory
		case1 = {'pencil':10, 'pen':8, 'paper':7}
		expected1 = {'pencil':20, 'pen':18, 'paper':17}
		self.assertEqual(func(case1), expected1)

	def test_filter_0_items(self):
		"""
		Tests lab4.filter_0_items()
		"""
		func = lab4.filter_0_items
		case1 = {'pencil':0, 'pen':-3, 'paper':-11}
		expected1 = {'pen':-3, 'paper':-11}
		self.assertEqual(func(case1), expected1)

	def test_average_grades(self):
		"""
		Tests lab4.average_grades()
		"""
		func = lab4.average_grades
		case1 = {'Michael':[100, 78, 88, 900/10],
		'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}
		expected1 = {'Josh':87.0, 'Daniel':79.0, 'Michael':89.0}
		self.assertEqual(func(case1), expected1)

if __name__ == '__main__':
	try:
		import lab4
		print("lab4.py module found. Testing...")
		unittest.main( )
	except ImportError:
		print("Missing lab4.py module")