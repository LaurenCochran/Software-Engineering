import System

#only add students to classes goggins teaches
def test_professor():
    database = System.System()
    database.login('goggins', 'augurrox')
    course1 = 'databses'
    course2 = "software_engineering"
    course_inserted= 'comp_sci'
    if course_inserted == course1 or course_inserted == course2:
        database.usr.add_student('yted91', course_inserted)
    else:
        assert False
