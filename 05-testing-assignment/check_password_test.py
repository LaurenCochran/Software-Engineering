import pytest
import System
import Professor

def test_check_password1():
    database = System.System()
    database.load_data()
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    res = database.check_password(username, password)
    assert res == False
    password = '12121*^^&as'
    res = database.check_password(username, password)
    assert res == False
    password = 1234
    res = database.check_password(username, password)
    assert res == False
    password = 'boomr345'
    res = database.check_password(username, password)
    assert res == True


