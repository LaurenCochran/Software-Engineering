import pytest
import System

def test_check_password(database):
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    database.login(username, password)

@pytest.fixture
def database_system():
    database = System.System()
    database.load_data()
    return database
