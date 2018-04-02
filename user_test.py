import unittest
from user import User

class TestUser(unittest.TestCase):
	'''
    Test class  that defines test cases for our accounts class behaviours.

	Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
	def setUp(self):
		'''
		set up method to clear before each test case.
		'''

		self.new_user = User("Peter Polle", "12345")

	def tearDown(self):
		'''
		Method that does clean up after each test case has run
		'''
		User.user_list = []

	def test_account_init(self):
		'''
		Test case to test if the object is initializzed properly
		'''
		self.assertEqual(self.new_user.login_name, "Peter Polle")
		self.assertEqual(self.new_user.password, "12345")
if __name__ == '__main__':
    unittest.main()
	    