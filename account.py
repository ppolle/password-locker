class Account:
	'''
	Class that generates new instances of accounts/credentials
	'''

	account_list = []

	def __init__(self,account_name,email,first_name,last_name,number):
		'''
		__init__ method that helps us define properties for our objects.

		'''

		self.account_name = account_name
		self.email = email
		self.fisrt_name = first_name
		self.last_name = last_name
		self.number = number