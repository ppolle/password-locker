#!/usr/bin/env python3.6
from account import Account
from user import User

def create_user_account(name,email,password):
	'''
	Function to create a new user
	'''
	new_user = User(name,email,password)

	return new_user

def save_user(user):
	'''
	Function to save User
	'''
	contact.save_user()

def user_login(login):
	'''
	Function to login users
	'''
	return User.user_login(login)

def create_account(account_name,email,user_name,number):
	'''
	Function to create a new account
	'''
	new_account = Account(account_name,email,user_name,number)
	return new_account
def save_account(account):
	'''
	Function to create new account
	'''
	account.save_account()
def delete_account(account):
	'''
	Function to delete an acount
	'''
	account.delete_account()

def find_account(number):
	'''
	Function that finds an account using th ephone number and returns the account
	'''
	return Account.find_by_number(number)

def check_if_account_exists(number):
	'''
	Function that checks if an account exists
	'''
	return Account.account_exist(number)
def display_accounts():
	'''
	Function that returns all saved contacts
	'''
	return Account.display_account()

def generate_password(pass_length):
	'''
	Function that generates a password
	'''
	return Account.generate_password(pass_length)
