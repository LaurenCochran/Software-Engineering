import System

def test_view_assignments():
    database = System.System()
    database.login('hdjsr7', 'pass1234')
    assignments = database.usr.view_assignments('databases')
    assert assignments[0] == ['assignment1', '1/6/20']
    assert assignments[1] == ['assignment2', '2/6/20']