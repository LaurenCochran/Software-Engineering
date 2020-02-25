import System

#should fail
def test_submit_assignment():
    database = System.System()
    database.login('hdjsr7', 'pass1234')
    database.usr.submit_assignment('cloud_computing', 'assignment2', 'this is a submission', '03/29/20')
    data = database.load_user_db()
    assert data['hdjsr7']['courses']['cloud_computing']['assignment2']['ontime'] == False
