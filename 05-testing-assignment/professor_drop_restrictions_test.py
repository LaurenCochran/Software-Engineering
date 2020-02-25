import System

#only add students to classes goggins teaches
def test_professor():
    database = System.System()
    database.login('saab', 'boomr345')
    course = 'comp_sci'
    course_inserted= 'software_engineering'
    if course_inserted == course:
        database.usr.drop_student('yted91', course_inserted)
    else:
        assert False