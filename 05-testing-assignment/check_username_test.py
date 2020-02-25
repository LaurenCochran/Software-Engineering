import System

def test_check_username():
    database = System.System()
    username= 'lacf66'
    password = '1234'
    database.login(username, password)
    database.reload_data()
    username = 'ase44'
    database.login(username, password)