#!/usr/bin/env python3.6
from account import account
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
