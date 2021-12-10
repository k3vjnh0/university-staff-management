import entity.staff as s
import entity.teacher as t
import entity.EDegree as deg
import entity.EPosition as pos


def calculate_allowance(employee):
    allowance = 0

    if isinstance(employee, s.Staff):
        if employee.get_position() == pos.Position(1).name:
            allowance = 2000

        if employee.get_position() == pos.Position(2).name:
            allowance = 1000

        if employee.get_position() == pos.Position(3).name:
            allowance = 500

    if isinstance(employee, t.Teacher):
        if employee.get_degree() == deg.Degree(1).name:
            allowance = 300

        if employee.get_degree() == deg.Degree(2).name:
            allowance = 500

        if employee.get_degree() == deg.Degree(3).name:
            allowance = 1000

    return allowance
