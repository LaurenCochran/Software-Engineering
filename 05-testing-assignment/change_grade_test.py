import pytest
import Staff
import User
import System


def test_change_grade():
    databaseSystem = System.System()
    databaseSystem.load_data()
    databaseSystem.login('cmhbf5', 'bestTA')
    databseSystem.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', 50)
    databaseSystem.reload_data()
    databaseSystem.login('hdjsr7', 'pass1234')
    grades = gradeSystem.usr.check_grades('cloud_computing')
    assert grades[0] == 50
