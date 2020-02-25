import System

def test_student_submit():
    database = System.System()
    username = 'hdjsr7'
    password = '1233'
    if len(password) > 4 and any(char.isalpha() for char in password):
        database.login('hdjsr7', password)
    else:
        assert False
