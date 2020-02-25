import System

def test_check_ontime():
    database = System.System()
    database.login('akend3', '123454321')
    database.usr.submit_assignment('comp_sci', 'assignment2', 'this is a resubmission', '03/29/20')
    data = database.load_user_db()
    assert data['akend3']['courses']['comp_sci']['assignment2']['ontime'] == 'false'