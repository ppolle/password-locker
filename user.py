class User:
	'''
	Class User to manage user data
	'''
	def __init__(self, login_name, password):
        '''
        this method ddefines properties for our user object
        '''
        self.login_name = login_name
        self.password = password