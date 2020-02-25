import System

def test_TA():
    database = System.System()
    database.login('cmhbf5', 'bestTA')
    course = "software_engineering"
    course_inserted = "databases"
    if course_inserted == course:
        database.usr.change_grade('akend3', course_inserted)
    else:
        assert False