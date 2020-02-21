import pytest
import System

def check_password_test(system):
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    system.login(username, password)

@pytest.fixture
def database_system():
    system = System.System()
    system.load_data()
    return database
