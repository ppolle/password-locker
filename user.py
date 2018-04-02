class User:
	'''
	Class that generates new instance of a user
	'''
	user_list = []

	def __init__(self, login_name, password):
		'''
		this method ddefines properties for our user object
		'''
		self.login_name = login_name
		self.password = password
	
	def save_user(self):
		'''
		saves user objects into user_list
		'''
		User.user_list.append(self)