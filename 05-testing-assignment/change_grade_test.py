import pytest
import Staff
import User
import System
import Student
import json


def test_change_grade():
    databaseSystem = System.System()
    databaseSystem.login('cmhbf5', 'bestTA')
    databaseSystem.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', 50)
    databaseSystem.reload_data()
    databaseSystem.login('hdjsr7', 'pass1234')
    databaseSystem.reload_data()
    grades = databaseSystem.usr.check_grades('cloud_computing')
    assert grades[0] == ['assignemnt1', 50]
