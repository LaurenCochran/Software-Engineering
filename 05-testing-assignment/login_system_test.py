import pytest
import System
import User
import Student

def test_login_system():
    database = System.System()
    database.login('hdjsr7', 'pass1234')
    database.load_data()
    user = database.load_user_db()
    users = database.usr
    assert users.name == "hdjsr7"
    assert user['hdjsr7']['role'] == 'student'
    assert users.password == 'pass1234'
