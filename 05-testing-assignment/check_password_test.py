import pytest
import System

def test_check_password(system):
    username = 'saab'
    password = 'notgoingtoworkhopefully'
    system.login(username, password)

@pytest.fixture
def database_system():
    system = System.System()
    system.load_data()
    return system
