import pytest
import System

def test_check_password1():
    database = System.System()
    database.load_data()
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    database.login(username, password)

def test_check_password2():
    database = System.System()
    database.load_data()
    username = 'saab'
    password = '12121*^^&as'
    database.login(username, password)

def test_check_password3():
    database = System.System()
    database.load_data()
    username = 'saab'
    password = 1234
    database.login(username, password)


