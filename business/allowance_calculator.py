import entity.staff
import entity.teacher
import entity.EDegree
import entity.EPosition


def calculate_allowance(employee):
    allowance = 0

    if isinstance(employee, entity.staff.Staff):
        if employee.get_position() == entity.EPosition.Position(1).name:
            allowance = 2000

        if employee.get_position() == entity.EPosition.Position(2).name:
            allowance = 1000

        if employee.get_position() == entity.EPosition.Position(3).name:
            allowance = 500

    if isinstance(employee, entity.teacher.Teacher):
        if employee.get_degree() == entity.EDegree.Degree(1).name:
            allowance = 300

        if employee.get_degree() == entity.EDegree.Degree(2).name:
            allowance = 500

        if employee.get_degree() == entity.EDegree.Degree(3).name:
            allowance = 1000

    return allowance
