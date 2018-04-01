import unittest
from account import Account

class TestAccount(unittest.TestCase):
    '''
    Test class  that defines test cases for our accounts class behaviours.

    Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to before each test case.
        '''

        self.new_account = Account("facebook", "peter.m.polle@gmail.com", "ppolle", "0725603607")

    def tearDown(self):
        '''
        Method that does clean up after each test case has run
        '''
        Account.account_list = []

    def test_account_init(self):
        '''
        test case to test if the object is initializzed properly
        '''
        self.assertEqual(self.new_account.account_name, "facebook")
        self.assertEqual(self.new_account.email, "peter.m.polle@gmail.com")
        self.assertEqual(self.new_account.user_name, "ppolle")
        self.assertEqual(self.new_account.number, "0725603607")



if __name__ == '__main__':
    unittest.main()
