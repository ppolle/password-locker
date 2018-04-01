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
	def delete_account(self):
		'''
		delete_account method deletes account
		'''
		Account.account_list.remove(self)


	@classmethod
	def find_by_number(cls, number):
		'''
    	Method that takes in an account number and returns credentials that match that number
    	'''
		for account in cls.account_list:
			if account.number == number:
				return number

	@classmethod
	def display_account(cls):
		'''
		method that returns the account list
		'''
		return cls.account_list
