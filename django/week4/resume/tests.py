from django.test import TestCase
from .models import Resume, Education, Experience

# Create your tests here.

class ResumeTestcase(TestCase):
	resume1 = None
	exp1 = None
	edu1 = None

	def setUp(self):
		"""
		Sets up testing fixture and creates objects to be used in future tests.
		"""

		self.resume1 = Resume.objects.create(first_name='First', last_name='Last')
		self.exp1 = Experience.objects.create(parent_resume=self.resume1, title='test_title', location='test_location', start_date='2001-01-01', end_date='2012-12-12', description='test_description')
		self.edu1 = Education.objects.create(parent_resume=self.resume1, institution_name='test_inst', location='test_location', degree='test_degree', major='test_major', gpa='100.0')

	def test_starting_conditions(self):
		"""
		Check if resume, experience, and education exist.
		"""
		self.assertIsInstance(self.resume1, Resume)
		self.assertIsInstance(self.exp1, Experience)
		self.assertIsInstance(self.edu1, Education)

	def test_get_full_name(self):
		"""
		Tests get_full_name() for Resume.
		"""
		case1 = self.resume1.get_full_name()
		expected1 = 'First Last'
		self.assertEqual(case1, expected1)


	def test_get_last_name_first_name(self):
		"""
		Tests get_last_name_first_name() for Resume.
		"""
		case1 = self.resume1.get_last_name_first_name()
		expected1 = 'Last, First'
		self.assertEqual(case1, expected1)
