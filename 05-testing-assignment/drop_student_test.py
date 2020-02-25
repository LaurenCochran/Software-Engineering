import System

def test_drop_student():
    database = System.System()
    database.load_data()
    database.login('goggins', 'augurrox')
    database.usr.drop_student('hdjsr7', 'databases')
    database.reload_data()
    data = database.load_user_db()
    assert data['hdjsr7']['courses'] != 'databases'
