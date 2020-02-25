import System

def test_add_student():
    database = System.System()
    database.load_data()
    database.login('goggins', 'augurrox')
    database.usr.add_student('hdjsr7', 'comp_sci')
    database.reload_data()
    data = database.load_user_db()
    assert data['hdjsr7']['courses']['comp_sci']['assignment1']['submission'] == 'N/A'

