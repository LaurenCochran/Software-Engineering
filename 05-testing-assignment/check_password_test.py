import pytest
import System

def test_check_password():
    database = System.System()
    database.load_data()
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    database.login(username, password)


