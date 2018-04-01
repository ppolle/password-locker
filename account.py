class Account:
	'''
	Class that generates new instances of accounts/credentials
	'''

	account_list = []

	def __init__(self,account_name,email,user_name,number):
		'''
		__init__ method that helps us define properties for our objects.

		'''

		self.account_name = account_name
		self.email = email
		self.user_name = user_name
		self.number = number

	def save_account(self):
		'''
		save-account method saves account objects into account_list
		'''
		Account.account_list.append(self)